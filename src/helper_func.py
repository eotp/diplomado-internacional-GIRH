def plot_nino_regions():
    
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs

    fig = plt.figure(figsize=(12,8))
    ax = plt.axes(projection=ccrs.Mollweide(-160))
    #ax.coastlines(); 
    ax.stock_img(); ax.gridlines()

    from shapely.geometry import Polygon
    nino12 = Polygon([(-90,0), (-80,0), (-80,-10), (-90,-10)])
    nino3 = Polygon([(-150,5), (-90,5), (-90,-5), (-150,-5)])
    nino34 = Polygon([(-170,5), (-120,5), (-120,-5), (-170,-5)])
    nino4 = Polygon([(-200,5), (-150,5), (-150,-5), (-200,-5)])
    ninos = [[x] for x in [nino12, nino3, nino34, nino4]]

    color = ['none', "orange", 'none', "green"]
    for e, nino in enumerate(ninos):
        ax.add_geometries(nino, ccrs.PlateCarree(), 
                          facecolor=color[e], linewidth=2,
                          edgecolor='k', alpha=0.6, label="sd")
    ax.text(-88, 2, "Nino\n1+2", transform=ccrs.PlateCarree())
    ax.text(-155, 7, "Nino 3.4", transform=ccrs.PlateCarree())
    ax.text(-125, 7, "Nino 3", transform=ccrs.PlateCarree())
    ax.text(-180, 7, "Nino 4", transform=ccrs.PlateCarree())
    ax.set_extent([-250, -40, -60, 60], crs=ccrs.PlateCarree())