import lightkurve as lk
import matplotlib.pyplot as plt

print("Starting the final demo script...")
print("Searching for Kepler-186f data...")

try:
    search_result = lk.search_lightcurve('Kepler-186f')

    # Download the single best dataset.
    print("Downloading the single best dataset...")
    lc = search_result[0].download()
    print("Data download complete.")

    # Prepare the data
    print("Preparing the light curve...")
    lc = lc.remove_outliers()

    # --- FINAL FIX ---
    # The downloaded file was missing metadata. We will provide it manually.
    period = 129.944  # Known orbital period for Kepler-186f in days
    t0 = 131.440      # Known transit time for Kepler-186f
    
    # "Fold" the light curve using our hardcoded values
    print(f"Folding the light curve with a period of {period} days...")
    folded_lc = lc.fold(period=period, epoch_time=t0)

    # Create and save the plot
    print("Creating the final plot for your presentation...")
    ax = folded_lc.plot(label=f'Kepler-186f (Period = {period:.3f} days)')
    ax.set_title('Confirmed Transit of Exoplanet Kepler-186f')
    plt.savefig('FINAL_Exoplanet_Transit_Plot.png')

    print("\nSUCCESS! Script finished.")
    print("A file named 'FINAL_Exoplanet_Transit_Plot.png' has been saved.")
    print("Use this plot for your final presentation!")

    plt.show()

except Exception as e:
    print("\n--- AN ERROR OCCURRED ---")
    print("An unexpected error occurred. This may be a persistent network issue.")
    print(f"Error details: {e}")