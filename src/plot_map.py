def plot_map(ds, values=None, contour=False, 
             max_value=350, min_value=-350, title=None, ax=None, **kwargs):
    levels = np.arange(min_value, max_value+50, 50)
    
    if ax is None:
        ax = plt.axes(projection=ccrs.Orthographic(-70,-15))
    
    p = ds["precipitation"].plot.contourf(ax=ax, transform=ccrs.PlateCarree(), 
                         vmin=min_value, vmax=max_value, 
                         center=0, levels=levels, extend="both", cmap="RdBu",  
                                          cbar_kwargs={'label': "Precipitación en mm"})
    ax.coastlines(color="red")
    ax.add_feature(cartopy.feature.BORDERS, edgecolor="red")
    ax.gridlines()
    ax.set_extent([-82, -68.5, 0.5, -18]); #x0, x1, y0, y1 
    if title is None:
        title =""
    elif isinstance(title, str):
        pass
    else:
        title = pd.to_datetime(ds.time.values).strftime("%Y-%m")
    ax.set_title(title, size=16)