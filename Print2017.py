"--setParameterRanges r=0,1"
"freezeParameters"
lumi=[
    'lumi_13TeV_2017',
    'lumi_13TeV_XY',
    'lumi_13TeV_LS',
    'lumi_13TeV_BBD',
    'lumi_13TeV_DB',
    'lumi_13TeV_BCC',
    'lumi_13TeV_GS',
]
btag=[
    'CMS_btag_jes',
    'CMS_btag_lf',
    'CMS_btag_hf',
    'CMS_btag_cferr1',
    'CMS_btag_cferr2',
    'CMS_btag_hfstats1_2017',
    'CMS_btag_hfstats2_2017',
    'CMS_btag_lfstats1_2017',
    'CMS_btag_lfstats2_2017',
]
lepton=[
    'CMS_eff_hwwtrigger_2017',
    'CMS_eff_e_2017',
    'CMS_scale_e_2017',
    'CMS_eff_m_2017',
    'CMS_scale_m_2017',
]
ak4=[
    'CMS_scale_JESAbsolute',
    'CMS_scale_JESBBEC1',
    'CMS_scale_JESEC2',
    'CMS_scale_JESFlavorQCD',
    'CMS_scale_JESHF',
    'CMS_scale_JESRelativeBal',
    'CMS_scale_JESAbsolute_2017',
    'CMS_scale_JESBBEC1_2017',
    'CMS_scale_JESEC2_2017',
    'CMS_scale_JESHF_2017',
    'CMS_scale_JESRelativeSample_2017',
    'CMS_ak8jet_res_j_2017',
    ]
ak8=[
    'CMS_ak8jet_scale_JESAbsolute',
    'CMS_ak8jet_scale_JESBBEC1',
    'CMS_ak8jet_scale_JESEC2',
    'CMS_ak8jet_scale_JESFlavorQCD',
    'CMS_ak8jet_scale_JESHF',
    'CMS_ak8jet_scale_JESRelativeBal',
    'CMS_ak8jet_scale_JESAbsolute_2017',
    'CMS_ak8jet_scale_JESBBEC1_2017',
    'CMS_ak8jet_scale_JESEC2_2017',
    'CMS_ak8jet_scale_JESHF_2017',
    'CMS_ak8jet_scale_JESRelativeSample_2017',
    'CMS_ak8jet_res_j_2017',
    'CMS_ak8jet_JMS_2017',
    'CMS_ak8jet_JMR_2017',

]

scalepdf=[
    'QCDscale_ggH_ACCEPT',
    'QCDscale_qqH_ACCEPT',
    'pdf_Higgs_gg_ACCEPT',
    'pdf_Higgs_qqbar_ACCEPT',
    'pdf_Higgs_gg',
    'pdf_Higgs_qqbar',
    'QCDscale_ggH',
    'QCDscale_qqH',
    'QCDscale_ttbar_ACCEPT',
    'QCDscale_wjets_ACCEPT',
    'QCDscale_WpH_ACCEPT',
    'QCDscale_WmH_ACCEPT',
    'QCDscale_ZH_ACCEPT',
    'pdf_ttbar_ACCEPT',
    'pdf_wjets_ACCEPT',
    'pdf_WpH_ACCEPT',
    'pdf_WmH_ACCEPT',
    'pdf_ZH_ACCEPT',
]
etc=[
    'CMS_eff_Wtag_2017',
    'CMS_scale_met_2017',
    'CMS_PU_2017',
    'PS_ISR',
    'PS_FSR',
    'UE_CP5',
    'mjjshape_2017',
    'ggWWnorm',
    'qqWWqqnorm',
    'CMS_eff_prefiring_2017',
]


group_dict={}

group_dict['all']=lumi+btag+ak4+ak8+lepton+scalepdf+etc
group_dict['lumi']=btag+ak4+ak8+lepton+scalepdf+etc
group_dict['btag']=lumi+ak4+ak8+lepton+scalepdf+etc
group_dict['ak4']=lumi+btag+ak8+lepton+scalepdf+etc
group_dict['ak8']=lumi+btag+ak4+lepton+scalepdf+etc
group_dict['lepton']=lumi+btag+ak4+ak8+scalepdf+etc
group_dict['scalepdf']=lumi+btag+ak4+ak8+lepton+etc
group_dict['etc']=lumi+btag+ak4+ak8+lepton+scalepdf

for group in group_dict:
    freeze="--freezeParameters "+(",".join(group_dict[group]))
    submit='(mkdir -p run_2017_indep_'+group+';cd run_2017_indep_'+group+';combineTool.py -m "115, 120, 125, 130, 140, 160, 180, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000" -M AsymptoticLimits --rAbsAcc 0 --setParameters sigma=0,fvbf=0.5 --run expected -d ../output/WS2017.indep.root --job-mode "condor" --sub-opts "accounting_group=group_cms" --boundlist ../../scripts/mssm_HWW_boundaries_v5.json '+freeze+') &> logs/submit_'+group+'_2017.log&'
    print '---',group,'---'
    print submit
