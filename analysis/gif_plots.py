#!/usr/bin/env python3
import imageio


def main():

    runs = [64, 44, 66, 48, 70, 50, 72, 54, 60, 42] #starting at 7.5mm so if doesn't show up in ppt at least will show a plot with alphas
    plot_dir = './plots/normScan/cal_normScan/'

    dsp_params = ['alp_energy_run', 'alp_AoE_run', 'alp_dcr_run', 'alp_AoE_vs_dcr_run', 'alp_dcr_vs_tp0_50_run', 'alp_1d_aoe_run',
                'alp_cut_energy_run', 'alp_cut_AoE_run', 'alp_cut_dcr_run', 'alp_cut_AoE_vs_dcr_run', 'alp_cut_dcr_vs_tp0_50_run', 'alp_cut__1d_aoe_run']
    outputs_files = ['energy.gif', 'aoeVsE.gif', 'dcrVsE.gif', 'aoeVsdcr.gif', 'dcrVstp0_50.gif', '1d_aoe.gif',
                'cut_energy.gif', 'cut_aoeVsE.gif', 'cut_dcrVsE.gif', 'cut_aoeVsdcr.gif', 'cut_dcrVstp0_50.gif', 'cut_1d_aoe.gif']

    dsp_gif(dsp_params, runs, plot_dir, outputs_files)

def dsp_gif(dsp_params, runs, plot_dir, outputs_files):

    for param, outfile in zip(dsp_params, outputs_files):
        images = []
        for run in runs:
            images.append(imageio.imread(f'{plot_dir}{param}{run}.png'))

        imageio.mimsave(f'{plot_dir}{outfile}', images, fps=3)
        print('Saving ', f'{plot_dir}{outfile}')


if __name__=="__main__":
    main()
