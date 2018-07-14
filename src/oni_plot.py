def plot_oni(df, min_max = None, vline=None, ax=None):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(13,4))
    
    oni_melted = pd.melt(df, id_vars="0", value_name="ONI", var_name="Month")
    oni_melted["Date"] = oni_melted.apply(lambda x: pd.to_datetime(str(x[0]) +"-"+ str(x["Month"])).to_period("M"), axis=1)
    oni = oni_melted[["Date", "ONI"]].sort_values("Date").reset_index(drop=True).set_index("Date")
    if min_max is not None:
        oni = oni[str(min_max[0]):str(min_max[1])]        

    oni.plot(ax=ax, color="k")
    ax.fill_between(oni.index, 0.5, oni.ONI, where=oni.ONI >= 0.5,color="red", label="El Nino", interpolate=True)
    ax.fill_between(oni.index, -0.5, oni.ONI, where=oni.ONI <= -0.5,color="blue", label="La Nina", interpolate=True)
    ax.grid()
    ax.legend()
    ax.set_ylim(-3,3)
    ax.set_title("Ocean Nino Index (ONI)", size=14)
    
    if vline is not None:
        ax.axvline(str(vline), color="green", linestyle="dashed");
        