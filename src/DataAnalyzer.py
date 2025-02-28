from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QInputDialog,
    QApplication,
    QLineEdit,
    QMainWindow
)
from PySide6.QtGui import QAction
import matplotlib.pyplot as plt
from astroML.datasets import (fetch_sdss_spectrum, 
                              fetch_sdss_sspp, 
                              fetch_dr7_quasar, 
                              fetch_nasa_atlas)
from astroML.plotting import MultiAxes
from astropy.visualization import hist
import numpy as np
import tensorflow_datasets as tfds
import astro_datasets
import tensorflow as tf
import os
import shutil
import PIL
import sys

    
class objWin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Obj Window")
          
        layout = QHBoxLayout()        
        self.plate_in = QLineEdit()
        plate_lbl = QLabel("plate")
        layout.addWidget(plate_lbl)
        layout.addWidget(self.plate_in)
        self.mjb_in = QLineEdit()
        mjb_lbl = QLabel("mjd")
        layout.addWidget(mjb_lbl)
        layout.addWidget(self.mjb_in)
        self.fiber_in = QLineEdit()
        fiber_lbl = QLabel("fiber")
        layout.addWidget(fiber_lbl)
        layout.addWidget(self.fiber_in)
        self.button = QPushButton("Enter")
        self.button.clicked.connect(self.get_text)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def get_text(self):
        plate_text = int(self.plate_in.text())
        mjb_text = int(self.mjb_in.text())
        fiber_text = int(self.fiber_in.text())
        
        return plate_text, mjb_text, fiber_text 
        
class DataAnalyzer(QMainWindow):  
    def __init__(self):
        super().__init__()
        self.build_ui()
        self.setWindowTitle("Data Analyzer")
        self.resize(1920,1080)
        
    def build_ui(self):      
        self.setWindowTitle("Pulldown Menu Example")
        menu_bar = self.menuBar()
        danalysis_menu = menu_bar.addMenu("Dataset Analysis")
      
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        
        # Create a Data Analysis menu
        # Add actions to the menu
        SDDS_action = QAction("SDSS", self)
        sdss_sspp_action = QAction("sdss_sspp", self)
        dr7_quasar_action = QAction("dr7_quasar", self)
        sloan_atlas_action = QAction("sloan_atlas", self)
        # add actions to menu
        danalysis_menu.addAction(SDDS_action)
        danalysis_menu.addAction(sdss_sspp_action)
        danalysis_menu.addAction(dr7_quasar_action)
        danalysis_menu.addAction(sloan_atlas_action)
        # connect actions
        SDDS_action.triggered.connect(self.SDDS)
        sdss_sspp_action.triggered.connect(self.sdss_sspp)
        dr7_quasar_action.triggered.connect(self.dr7_quasar)
        sloan_atlas_action.triggered.connect(self.atlas)
        # create a Image Database menu
        iDatabase = menu_bar.addMenu("Image Database")
        slc_action = QAction("slc", self)
        planetary_objs_action = QAction("Planetary Objects", self)
        # add actions to menu
        iDatabase.addAction(slc_action)
        iDatabase.addAction(planetary_objs_action)
        # connect actions
        slc_action.triggered.connect(self.slc)
        planetary_objs_action.triggered.connect(self.planetary_objs)
        self.layout.setMenuBar(menu_bar)

    def SDDS(self):      
        #plate, mjd, fiber = int(self.planetary_objs())

        plate = 1615
        mjd = 53166
        fiber = 513
        print(plate, mjd, fiber)
        
        spec = fetch_sdss_spectrum(plate, mjd, fiber)

        #------------------------------------------------------------
        # Plot the resulting spectrum
        ax = plt.axes()
        ax.plot(spec.wavelength(), spec.spectrum, '-k', label='spectrum')
        ax.plot(spec.wavelength(), spec.error, '-', color='gray', label='error')
        ax.legend(loc=4)
        ax.set_title('Plate = %(plate)i, MJD = %(mjd)i, Fiber = %(fiber)i' % locals())
        ax.text(0.05, 0.95, 'z = %.2f' % spec.z, size=16,
                ha='left', va='top', transform=ax.transAxes)
        ax.set_xlabel(r'$\lambda (\AA)$')
        ax.set_ylabel('Flux')
        ax.set_ylim(-10, 300)
        plt.show()

    def sdss_sspp(self):
        print("sdss sspp")
        data = fetch_sdss_sspp()
        # do some reasonable magnitude cuts
        rpsf = data['rpsf']
        data = data[(rpsf > 15) & (rpsf < 19)]
        # get the desired data
        logg = data['logg']
        Teff = data['Teff']
        FeH = data['FeH']
        #------------------------------------------------------------
        # Plot the results using the binned_statistic function
        from astroML.stats import binned_statistic_2d
        N, xedges, yedges = binned_statistic_2d(Teff, logg, FeH,
                                                'count', bins=100)
        FeH_mean, xedges, yedges = binned_statistic_2d(Teff, logg, FeH,
                                                    'mean', bins=100)
        # Define custom colormaps: Set pixels with no sources to white
        cmap = plt.cm.jet
        cmap.set_bad('w', 1.)
        cmap_multicolor = plt.cm.jet
        cmap_multicolor.set_bad('w', 1.)
        # Create figure and subplots
        fig = plt.figure(figsize=(8, 4))
        fig.subplots_adjust(wspace=0.25, left=0.1, right=0.95,
                            bottom=0.07, top=0.95)
        #--------------------
        # First axes:
        plt.subplot(121, xticks=[4000, 5000, 6000, 7000, 8000])
        plt.imshow(np.log10(N.T), origin='lower',
                extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                aspect='auto', interpolation='nearest', cmap=cmap)
        plt.xlim(xedges[-1], xedges[0])
        plt.ylim(yedges[-1], yedges[0])
        plt.xlabel(r'$\mathrm{T_{eff}}$')
        plt.ylabel(r'$\mathrm{log(g)}$')

        cb = plt.colorbar(ticks=[0, 1, 2, 3],
                        format=r'$10^{%i}$', orientation='horizontal')
        cb.set_label(r'$\mathrm{number\ in\ pixel}$')
        plt.clim(0, 3)

        #--------------------
        # Third axes:
        plt.subplot(122, xticks=[4000, 5000, 6000, 7000, 8000])
        plt.imshow(FeH_mean.T, origin='lower',
                extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]],
                aspect='auto', interpolation='nearest', cmap=cmap_multicolor)
        plt.xlim(xedges[-1], xedges[0])
        plt.ylim(yedges[-1], yedges[0])
        plt.xlabel(r'$\mathrm{T_{eff}}$')
        plt.ylabel(r'$\mathrm{log(g)}$')

        cb = plt.colorbar(ticks=np.arange(-2.5, 1, 0.5),
                        format=r'$%.1f$', orientation='horizontal')
        cb.set_label(r'$\mathrm{mean\ [Fe/H]\ in\ pixel}$')
        plt.clim(-2.5, 0.5)

        # Draw density contours over the colors
        levels = np.linspace(0, np.log10(N.max()), 7)[2:]
        plt.contour(np.log10(N.T), levels, colors='k', linewidths=1,
                    extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
        plt.show()

    def dr7_quasar(self):
        print("Save file")
        data = fetch_dr7_quasar()

        colors = np.empty((len(data), 5))
        colors[:, 0] = data['mag_u'] - data['mag_g']
        colors[:, 1] = data['mag_g'] - data['mag_r']
        colors[:, 2] = data['mag_r'] - data['mag_i']
        colors[:, 3] = data['mag_i'] - data['mag_z']
        colors[:, 4] = data['mag_z'] - data['mag_J']

        labels = ['u-g', 'g-r', 'r-i', 'i-z', 'z-J']

        bins = [np.linspace(-0.4, 1.0, 100),
                np.linspace(-0.4, 1.0, 100),
                np.linspace(-0.3, 0.6, 100),
                np.linspace(-0.4, 0.7, 100),
                np.linspace(0, 2.2, 100)]

        ax = MultiAxes(5, wspace=0.05, hspace=0.05,
                    fig=plt.figure(figsize=(10, 10)))
        ax.density(colors, bins)
        ax.set_labels(labels)
        ax.set_locators(plt.MaxNLocator(5))
        plt.suptitle('SDSS DR7 Quasar Colors', fontsize=18)
        plt.show()

    def atlas(self):
        data = fetch_nasa_atlas()
        #------------------------------------------------------------
        # plot the RA/DEC in an area-preserving projection
        RA = data['RA']
        DEC = data['DEC']
        # convert coordinates to degrees
        RA -= 180
        RA *= np.pi / 180
        DEC *= np.pi / 180

        ax = plt.axes(projection='mollweide')
        plt.scatter(RA, DEC, s=1, c=data['Z'], cmap=plt.cm.copper,
                    edgecolors='none', linewidths=0)
        plt.grid(True)
        plt.title('NASA Atlas Galaxy Locations')
        cb = plt.colorbar(cax=plt.axes([0.05, 0.1, 0.9, 0.05]),
                        orientation='horizontal',
                        ticks=np.linspace(0, 0.05, 6))
        cb.set_label('redshift')
        #------------------------------------------------------------
        # plot the r vs u-r color-magnitude diagram
        absmag = data['ABSMAG']

        u = absmag[:, 2]
        r = absmag[:, 4]

        plt.figure()
        ax = plt.axes()
        plt.scatter(u - r, r, s=1, lw=0, c=data['Z'], cmap=plt.cm.copper)
        plt.colorbar(ticks=np.linspace(0, 0.05, 6)).set_label('redshift')
        plt.xlim(0, 3.5)
        plt.ylim(-10, -24)
        plt.xlabel('u-r')
        plt.ylabel('r')
        #------------------------------------------------------------
        # plot a histogram of the redshift
        plt.figure()
        hist(data['Z'], bins='knuth',
            histtype='stepfilled', ec='k', fc='#F5CCB0')
        plt.xlabel('z')
        plt.ylabel('N(z)')
        plt.show()
             
    def normalize(image, label):  
        image = (image - 4.3368458e-13) / 5.503901e-12
        return image, label

    def slc(self):
        # load mirabest imgames and info
        tds_slc, info_train = tfds.load(name='slc/space', split='train', with_info=True, as_supervised=True)
        #mirabest_img, info_train = tfds.load(name='mirabest/all', 
        #                                 split='train', with_info=True, as_supervised=True)
        def normalize(image, label):  
            image = (image - 4.3368458e-13) / 5.503901e-12
            return image, label
        # convert images to float
        tds_slc = tds_slc.map(normalize)
        
        for d in tds_slc.take(8):
            inputs, label = d
            print(label)
            plt.figure(figsize=(6, 6))
            plt.imshow(inputs[:,:,0])
            plt.show()

    def open_new_window(self):
            self.setWindowTitle("Another Window")
            layout = QVBoxLayout()
            label = QPushButton("This is another window.")
            layout.addWidget(label)
            self.setLayout(layout)
        
    def planetary_objs(self):
        self.setWindowTitle("Another Window")
        layout = QVBoxLayout()
        label = QPushButton("This is another window.")
        layout.addWidget(label)
        self.setLayout(layout) 
        self.new_window = objWin()
        self.new_window.show()
         
    def mirabell(self):
        mirabell_img, info_train = tfds.load(name='mirabest/all', split='train', with_info=True, as_supervised=True) 

        def img_to_float32(image, label):
            return tf.image.convert_image_dtype(image, tf.float32), label
        
        mirabell_img = mirabell_img.map(img_to_float32)
        for d in mirabell_img.take(2):
            inputs, label = d
            print(label)
            plt.figure(figsize=(6, 6))
            plt.imshow(inputs[:,:,0])
            plt.show()

    def mlsst(self):
        mlsst_img, info_mlsst = tfds.load(name='mlsst/Y10', split='train', with_info=True, as_supervised=True)
        
        def normalize(image, label):  
            image = tf.math.asinh(image)
            image -= tf.constant(tf.mean, shape=[1, 1, 3], dtype=image.dtype)
            image /= tf.constant(tf.std, shape=[1, 1, 3], dtype=image.dtype)
            return image, label

        mlsst_img = mlsst_img.map(normalize())
        
        for d in mlsst_img.take(2):
            inputs, label = d
            print(label)
            print(inputs.shape)
            plt.figure(figsize=(6, 6))
            plt.imshow(inputs[:,:,0])
            plt.show()
            
    def sn1a(self):       
        CMD_FIELDS = ['Mtot', 'Mtot_Nbody', 'HI', 'Mcdm', 'Mgas', 'MgFe', 'Mstar', 'ne', 'P', 'T', 'Vcdm',
                      'Vgas', 'Z']       
 
        def resize(image, label, size):
            image = tf.image.resize(image, size=[size, size])
            return image, label
        
        def normalize(image, label):  
            image = tf.math.asinh(image)
            image = image - 26
            return image, label
                    
        ds, info = tfds.load(name='cmd', 
                     split='train', 
                     with_info=True, 
                     as_supervised=True, 
                     builder_kwargs={'simulation': 'IllustrisTNG', 'field': 'Mtot_Nbody', 
                                     'parameters': ['omegam']})
 
        ds = ds.map(lambda image, label: resize(image, label, 64))
        ds = ds.map(normalize)
        
        for d in ds.take(2):
            inputs, label = d
            print(label)
            plt.figure(figsize=(6, 6))
            plt.imshow(inputs[:,:,0])
            plt.show()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DataAnalyzer()
    main_window.show()
    sys.exit(app.exec())
    