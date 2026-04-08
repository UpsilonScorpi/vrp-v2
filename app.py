from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore, QtNetwork, QtGui
import sys

class MiniWeb(QtWidgets.QWidget):
    def __init__(self, url, cookie_name, cookie_value, domain, path="/"):
        super().__init__()
        self.setWindowTitle("VRP - v2")
        self.setWindowIcon(QtGui.QIcon("scorpion.png"))
        self.setWindowFlags(
            self.windowFlags() |
            QtCore.Qt.Window |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowSystemMenuHint |
            QtCore.Qt.WindowStaysOnTopHint
        )
        self.setFixedSize(400, 300)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.profile = QtWebEngineWidgets.QWebEngineProfile("MiniWebProfile", self)
        self.cookie_store = self.profile.cookieStore()
        self.inject_cookie(cookie_name, cookie_value, domain, path)
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.setPage(QtWebEngineWidgets.QWebEnginePage(self.profile, self))
        self.browser.setUrl(QtCore.QUrl(url))
        layout.addWidget(self.browser)

    def inject_cookie(self, name, value, domain, path):
        cookie = QtNetwork.QNetworkCookie()
        cookie.setName(name.encode())
        cookie.setValue(value.encode())
        cookie.setDomain(domain)
        cookie.setPath(path)
        cookie.setSecure(True)
        self.cookie_store.setCookie(cookie)

    def move_bottom_right(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        title_height = self.style().pixelMetric(QtWidgets.QStyle.PM_TitleBarHeight)
        x = screen.right() - self.width()
        y = screen.bottom() - self.height() - title_height
        self.move(x, y)

app = QtWidgets.QApplication(sys.argv)

window = MiniWeb(
    url="https://versaillesrp-v2.fr/admin_erlc_manager.php",
    cookie_name="PHPSESSID",
    cookie_value="SESSION_ID",
    domain=".versaillesrp-v2.fr",
    path="/"
)

window.show()
window.move_bottom_right()
sys.exit(app.exec_())
