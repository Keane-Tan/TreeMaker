import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/0631086E-BFBE-E611-A105-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/067C3388-9DBE-E611-8F93-0CC47A4D761A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/0E7B727C-95BE-E611-AEEB-0CC47A4C8E34.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/16B16D77-9DBE-E611-B50F-0CC47A4D76CC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/1A5087DC-94BE-E611-9F9C-0CC47A4D7668.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/1C9EA8D6-A1BE-E611-A0A9-0025905A60B8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/2000A15F-9CBE-E611-9C9D-0CC47A4D764A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/24906C86-9DBE-E611-9F79-0CC47A4C8F0C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/2864E2E2-A2BE-E611-8DB3-0025905B8574.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/3663C670-BFBE-E611-86DF-0025905B85C6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/3A90ECF2-9FBE-E611-AB28-0CC47A7C356A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/4219D561-9EBE-E611-BFCC-0025905A60E4.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/44C0E1F0-9ABE-E611-988B-0CC47A78A3D8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/46E86F99-99BE-E611-8F01-0025905A60A6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/4CA14557-9CBE-E611-BD03-0CC47A4D7600.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/4CF4EA35-98BE-E611-8199-0CC47A78A446.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/4E40AE65-A2BE-E611-B14A-0CC47A78A436.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/5064F943-85BE-E611-B8C3-0CC47A78A414.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/5630D7FD-98BE-E611-AAAB-0025905A611C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/58E0C11C-A1BE-E611-A1B1-0CC47A4C8F0C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/5C0A9F8C-99BE-E611-9CFA-0CC47A78A436.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/6299601F-A1BE-E611-A9F4-0025905B85B6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/66BA1B19-9ABE-E611-9D83-0025905B85A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/68ED6DFF-9FBE-E611-B4EF-0025905A497A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/6AC74225-A1BE-E611-9168-0025905B8582.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/6EB079FC-96BE-E611-94C2-0025905A60AA.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/781C71A0-99BE-E611-9016-0025905A4964.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/7CA6317D-96BE-E611-8945-0CC47A4C8E8A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/8638DF06-9BBE-E611-8F72-0CC47A7C34B0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/8C5EB73C-98BE-E611-89A6-0CC47A4D76D6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/925D66C8-9EBE-E611-88E4-0025905A60A6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/98A2E4CA-9BBE-E611-8870-0CC47A4C8EA8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/9A114B1D-9ABE-E611-AB04-0025905A607E.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/9AEE0400-99BE-E611-B556-0025905A6068.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/9E011D7F-95BE-E611-8631-0025905A60F2.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/A473DBCE-9BBE-E611-B403-0025905A6056.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/A60A93B9-97BE-E611-96B8-0CC47A745250.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/AC650064-9CBE-E611-A3D9-0CC47A78A340.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/AEB60D7B-9DBE-E611-B0CD-0025905B8564.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/B690B55E-9EBE-E611-954D-0025905B8572.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/B8BAF188-9DBE-E611-A108-0CC47A4D7614.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/BA6C2EF7-98BE-E611-95FB-0CC47A7C34E6.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/C4BD7B37-9CBE-E611-96AD-0025905A60DE.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/CE23603C-98BE-E611-9D19-0CC47A4D7600.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/D0D3BE8A-9DBE-E611-B7C7-0CC47A78A446.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/D456BE1B-9ABE-E611-A8CE-0CC47A4D7632.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/D6C2C704-99BE-E611-B9AF-0CC47A78A4A0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/D6FA2DFA-96BE-E611-9D65-0025905B8574.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/D82947B7-A3BE-E611-9AA2-0CC47A4D7640.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/DA80FF7E-9DBE-E611-A2B1-0025905B8592.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/DA8F85BB-A3BE-E611-ABE7-0CC47A74525A.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/E6CF89B8-97BE-E611-AB09-0CC47A4D760C.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/EA9026D2-9EBE-E611-92E0-0CC47A4D7674.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/F0C96FC8-93BE-E611-A17B-0CC47A4C8EE8.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/F879517A-9DBE-E611-99F3-0CC47A7C3432.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/60000/FC758E08-9BBE-E611-B932-0CC47A4C8E70.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/70F65588-91BE-E611-A499-441EA1733CCC.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/980D9C1C-91BE-E611-B7EA-0025905A60B0.root',
       '/store/mc/RunIISummer16MiniAODv2/TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/80000/FE4680D1-8FBE-E611-9110-0025905B861C.root',
] )