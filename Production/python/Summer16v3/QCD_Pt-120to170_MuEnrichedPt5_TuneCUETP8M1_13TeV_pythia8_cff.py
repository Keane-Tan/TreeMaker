import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0058A056-B5E3-E811-BFF9-0025905D1D52.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/00E06F77-B5E3-E811-9197-0CC47AF9B2D2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/02CC147B-B0E3-E811-81F3-0025904C68DC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/02EE5E5D-ADE3-E811-A474-0CC47AF9B32A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/0E1ED138-BAE3-E811-8E69-0025905C542C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1A9BA97F-A3E3-E811-ADCD-0025905C3D40.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1AED5D7E-99E3-E811-9502-0CC47AF9B1D6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/1C88AC70-9DE3-E811-8F27-0CC47AFB7D60.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/22188382-A6E3-E811-B23D-0025905C542C.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/24C44E1F-9FE3-E811-A5D9-0025905C3D96.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2AF5B96B-BAE3-E811-9FD1-0CC47AFB7D80.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/2C6BDC9F-9BE3-E811-9D26-0025904C68DA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/30059180-9FE3-E811-89D1-0025905C5484.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3042B117-A1E3-E811-989F-0CC47AFB7D08.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/32A8C41B-9FE3-E811-924A-0025905C5476.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/34ED85ED-B5E3-E811-8347-0025905C2CE6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/365D41F2-B5E3-E811-B42E-0025905C3DCE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3C36DC68-ACE3-E811-A56B-0025905D1CB4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/3EE3D375-BCE3-E811-BF65-0CC47AFB80B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/42FAE9A4-B1E3-E811-AD18-0CC47AFB81B4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/44290B55-AAE3-E811-B9C5-0025905D1E02.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5403E52D-AEE3-E811-8A9B-0025905C2CEA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/58D1A4C3-A4E3-E811-AEC0-0025905D1CB2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5CF31CA3-A4E3-E811-9AC0-0025905D1E00.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/5EEBBCEB-99E3-E811-A12A-0CC47AF9B1AA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/60A67970-AAE3-E811-AFEC-0CC47AF9B2BE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/60CE44C1-B1E3-E811-9987-0025905C2CD0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/60D4E88B-97E3-E811-BF4D-0025905C42A8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/629C0680-C0E3-E811-A829-0025904C51D8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/64F8EA9E-A5E3-E811-96A2-0025904C6376.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/66AD9DA2-A1E3-E811-A675-0025905C53DE.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/6A5BF8CF-9EE3-E811-805F-0CC47AF9B1AA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/706E7144-B6E3-E811-B330-0025905C3DF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/7AFD2923-9FE3-E811-BA5E-0025905C53A4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/8265F994-A7E3-E811-81EB-0025904C67A4.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/86D4CF07-A0E3-E811-AC4D-0025905C4262.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/88ADDFE8-B5E3-E811-B1AC-0025905C2CD2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9018E561-97E3-E811-8E62-0CC47AFB7D80.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/94D67B1F-9FE3-E811-BC6F-0025905C53A8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/9ABE3EA8-A6E3-E811-8BFA-0025904C637A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/A2898047-C0E3-E811-9E73-0025905C3DF8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/BADDF65B-B5E3-E811-9CED-0025905C53F2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/BC8A1D67-9DE3-E811-876B-0CC47AFB81BC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C6B73A00-ABE3-E811-B5B6-0025905D1CB0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/C6D94FCC-98E3-E811-B613-0CC47AFB7CEC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/CA1DD9C9-97E3-E811-84A8-0025905D1CB6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D21031EF-B5E3-E811-ACB7-0025905C54C6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D2269F8E-B5E3-E811-BC75-0025904C637E.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D28E90EE-B5E3-E811-B486-0025905C95F8.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D2B96F6F-A8E3-E811-971F-0CC47AF9B2BA.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/D8AE2584-BFE3-E811-89EA-0025905D1CB6.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E034D162-C0E3-E811-A2EF-0CC47AF9B496.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E4709C3A-97E3-E811-82DE-0CC47AFB80B0.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/E89001AD-9BE3-E811-B77D-0CC47AFB7D90.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/EE0AA87B-A6E3-E811-93BA-0025905C42A2.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/F4B6D83B-9FE3-E811-BCD7-0025904B7C26.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/FA6CA195-98E3-E811-8845-0025904C650A.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/FCEFC5A4-BCE3-E811-9825-0CC47AFB7DCC.root',
       '/store/mc/RunIISummer16MiniAODv3/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/120000/FE4ECE55-98E3-E811-A2FA-0025905C2D9A.root',
] )
