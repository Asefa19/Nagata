from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMenu,
    QMenuBar,
    QSizePolicy,
    QInputDialog,
    QApplication,
    QLineEdit
)
from PySide6.QtGui import QAction
from matplotlib import pyplot as plt
from astroML.datasets import fetch_sdss_spectrum, fetch_sdss_sspp 
#fetch_dr7_quasar
#from astroML.plotting import MultiAxes
import numpy as np


class DataAnalyzer(QWidget):
    
    def __init__(self):
        super().__init__()
        self.build_ui()
        
        self.setWindowTitle("Data Analyzer")
        self.resize(1920,1080)
        
    def build_ui(self):
        
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        # Create a menu
        menu = QMenu("Dataset Analysis", self)

        # Add actions to the menu
        SDDS_action = QAction("SDSS", self)
        sdss_sspp = QAction("sdss_sspp", self)
        dr7_quasar_action = QAction("dr7_quasar", self)
        exit_action = QAction("Exit", self)

        menu.addAction(SDDS_action)
        menu.addAction(sdss_sspp)
        menu.addAction(dr7_quasar_action)
        menu.addAction(exit_action)

        SDDS_action.triggered.connect(self.SDDS)
        sdss_sspp.triggered.connect(self.sdss_sspp)
        dr7_quasar_action.triggered.connect(self.dr7_quasar)
        exit_action.triggered.connect(self.exit_app)

        # Create a button to show the menu
        menu_button = QPushButton("File", self)
        menu_button.setMenu(menu)
        self.layout.addWidget(menu_button)

        # Create a menu bar
        menu_bar = QMenuBar(self)
        menu_bar.addMenu(menu)
        menu_bar.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        menu_bar.setFixedHeight(50) # Set fixed height
        self.layout.setMenuBar(menu_bar)

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get Text", "Enter your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.text_edit.setText(text)


    def SDDS(self):
        plate = 1615
        mjd = 53166
        fiber = 513

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
        # data = fetch_dr7_quasar()

        # colors = np.empty((len(data), 5))

        # colors[:, 0] = data['mag_u'] - data['mag_g']
        # colors[:, 1] = data['mag_g'] - data['mag_r']
        # colors[:, 2] = data['mag_r'] - data['mag_i']
        # colors[:, 3] = data['mag_i'] - data['mag_z']
        # colors[:, 4] = data['mag_z'] - data['mag_J']

        # labels = ['u-g', 'g-r', 'r-i', 'i-z', 'z-J']

        # bins = [np.linspace(-0.4, 1.0, 100),
        #         np.linspace(-0.4, 1.0, 100),
        #         np.linspace(-0.3, 0.6, 100),
        #         np.linspace(-0.4, 0.7, 100),
        #         np.linspace(0, 2.2, 100)]

        # ax = MultiAxes(5, wspace=0.05, hspace=0.05,
        #             fig=plt.figure(figsize=(10, 10)))
        # ax.density(colors, bins)
        # ax.set_labels(labels)
        # ax.set_locators(plt.MaxNLocator(5))
        # plt.suptitle('SDSS DR7 Quasar Colors', fontsize=18)
        # plt.show()


    def exit_app(self):
        QApplication.instance().quit()

        
        self.setStyleSheet("""
                           QWidget{
                               background-color: #f0f0f0;
                               font-family: Arial;
                            }
                            QPushButton{
                                background-color: #0078d4;
                                color: white;
                                padding: 8px;
                                border-radius:4px;
                            }
                            """)
        
        
