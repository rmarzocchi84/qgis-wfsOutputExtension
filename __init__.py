"""
/***************************************************************************
    QGIS Server Plugin Filters: Add Output Formats to GetFeature request
    ---------------------
    Date                 : October 2015
    Copyright            : (C) 2015 by René-Luc D'Hont - 3Liz
    Email                : rldhont at 3liz dot com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS and QGIS Server.
"""

def serverClassFactory(serverIface):
    """Load wfsOutputExtensionServer class from file wfsOutputExtension.

    :param iface: A QGIS Server interface instance.
    :type iface: QgsServerInterface
    """
    #
    from .wfsOutputExtensionServer import wfsOutputExtensionServer
    return wfsOutputExtensionServer(serverIface)
