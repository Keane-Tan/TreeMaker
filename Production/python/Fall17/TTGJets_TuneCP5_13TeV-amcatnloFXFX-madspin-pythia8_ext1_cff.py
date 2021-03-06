import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/0279BF79-025A-E811-A63F-FA163EFF978D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/06B6583A-8B59-E811-80E0-FA163E2B9C34.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/0A71A251-8959-E811-A5E5-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/0EF9423D-9459-E811-97CC-FA163E36B86F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/1E01AF5B-8859-E811-A0F7-FA163E60F9F7.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/247BBBEA-8A59-E811-B2A5-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/28A09EF7-8559-E811-833B-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/2C295430-9C59-E811-B89C-FA163E4F0E53.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/340AF21B-8E59-E811-8321-FA163EACE1E5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/3AAA3198-9F59-E811-BD71-FA163E86F10A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/4626BACC-8C59-E811-A2A8-FA163EDA9606.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/48319A55-9459-E811-BCA6-FA163E51AE81.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/48AF5020-7259-E811-8215-FA163ED77E96.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/4C9AED95-8E59-E811-8B94-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/4EE165C0-A259-E811-B6C6-FA163E010CF9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/50977EBA-8C59-E811-8D8D-FA163E73F4B9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/509A4886-8F59-E811-A9C6-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/52979CB1-A759-E811-BCC9-FA163E3E546D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/52ADAEAA-8659-E811-9A8A-FA163E3E546D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/54678968-8C59-E811-9ED6-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/549D2007-AD59-E811-BC3A-FA163EAD8059.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/683371B0-8659-E811-AB41-FA163E10084A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/68A52A45-A359-E811-BC03-FA163E6F7000.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/6C3678D9-9559-E811-94BB-FA163E852F59.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/6E613DF7-8A59-E811-9685-FA163E10084A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/6E6DEFB1-B759-E811-BA65-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/7499D523-9759-E811-8333-FA163E36B86F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/78D2C641-9159-E811-A003-FA163E9D6ED9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/8282695A-9459-E811-9C19-FA163E51AE81.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/8A5F686D-8959-E811-884C-FA163E759636.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/8CD1B3C1-9859-E811-85DA-FA163EF125F4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/92D98D2F-8959-E811-8879-FA163EF066B9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/9818E4E3-7A59-E811-9920-FA163EAF4D44.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/982FED35-8B59-E811-A850-FA163E2B9C34.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/9A3C2B9A-7A59-E811-8F25-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/9E384C61-9759-E811-AA90-FA163EE06C6D.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/A601657E-9A59-E811-BB5A-FA163EECEE39.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/A675F607-8E59-E811-B30C-FA163E605F3F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/A8BAAF67-9759-E811-AA60-FA163E4BEFFB.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/AAF7F92A-9159-E811-A2D5-FA163E9D6ED9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/AE91492E-9159-E811-B321-FA163EE24D0F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/B0092D47-8E59-E811-B89B-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/B0148E9C-8659-E811-A0F9-FA163EDA9606.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/B08D547E-9259-E811-9C27-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/B0B27997-7A59-E811-87C2-FA163EDA9606.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/B8574C7B-8F59-E811-A71F-FA163E01E788.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/BE9EE46F-9259-E811-84F5-FA163EDA9606.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/CCD3AE27-9159-E811-B33A-FA163E36B86F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/CE3A0772-8F59-E811-BC99-FA163EDA9606.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/D270889E-7F59-E811-9A1C-FA163E501CAF.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/D40F7A48-8959-E811-8458-FA163EF066B9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/D4C53E6B-8C59-E811-AE29-FA163E01E788.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/D8F9A782-9259-E811-8CE3-FA163EBCF443.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/DE5B05ED-8A59-E811-80EC-FA163E605F3F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/DE61D49C-9259-E811-B347-FA163E876D8E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/EC9B73F9-8559-E811-93FD-FA163E605F3F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/F200412A-8659-E811-8004-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/F6F2D1C7-9859-E811-BDE4-FA163E823CC5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/30000/F8897B7E-9A59-E811-A979-FA163EE4A782.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/0001E7BA-DC59-E811-A87B-FA163E17FD8B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/06A7B919-9659-E811-A042-FA163E34D5EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/084821FE-0F5A-E811-A557-FA163E587A6B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/0EFF3809-BD59-E811-9C2E-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/108D5BB9-DC59-E811-A979-FA163EBB80A0.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/10AEFECD-B859-E811-BE2F-FA163E6754BE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/18E2AC15-275A-E811-962B-FA163EF49570.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/1AAC91BA-305A-E811-8F9E-FA163E162D4E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/1AD80C41-9A59-E811-A680-FA163E6D83D5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/1ED9BAE1-A059-E811-B23C-FA163EA0FCDA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/229F6F17-A159-E811-B41A-FA163E7AF728.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/26CDDF3F-9A59-E811-9F6E-FA163EBAD941.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/282E75F5-095A-E811-B3AE-FA163EBA0612.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/30B72CA0-D059-E811-A1CB-FA163E17FD8B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/30C81B1B-A159-E811-80B4-FA163E34D5EC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/32921670-1B5A-E811-AC77-FA163E49583C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/36A8D05D-B459-E811-AA20-FA163EF26FC6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/382FCE41-8B59-E811-AE75-FA163EACE1E5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/3AAE4BE7-BE59-E811-BC8A-FA163E60D6CC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/3CBFF909-8159-E811-B6BB-FA163E4DAB5E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/427E1D04-B259-E811-B298-FA163EFC2B18.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/4618B635-9A59-E811-A502-FA163EB50606.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/48672D53-D759-E811-977C-FA163E57B050.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/4873C111-A159-E811-AB44-FA163EE837AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/48DD67E9-9559-E811-A5B3-FA163E3D9D36.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/4E5FF2BF-065A-E811-B30E-FA163E02C124.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/50370358-155A-E811-8D51-FA163E162D4E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/5265EB0E-A159-E811-980A-FA163EA06439.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/52B9F99B-295A-E811-B141-FA163E2BBDCE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/52E2CF11-A159-E811-A601-FA163E4BE110.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/540DA6E0-0F5A-E811-97E1-FA163EF91419.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/5E2F2844-9A59-E811-93C1-FA163E6B64D8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/60FA4C01-FF59-E811-8B60-FA163EBB53AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/623E08FA-BE59-E811-B8FA-FA163E759636.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/66107E5B-A859-E811-8BBC-FA163E605F3F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/6885BCDA-A059-E811-97E1-FA163E3C37E9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/68D46F43-9A59-E811-A711-FA163E337EE8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/6AA48860-8859-E811-B4CB-FA163E605F3F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/6C1CE525-A159-E811-BFCD-FA163E54FE55.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/70417852-9A59-E811-BF6F-FA163E81E791.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/7C02A437-C159-E811-9333-FA163EDE0D24.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/7CB09B09-9559-E811-906D-FA163E451BF7.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/7CB1E540-9A59-E811-8E30-FA163E4137CD.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/7CC5CE0C-EA59-E811-8D37-FA163E8A8A51.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/7E6B2EE8-B159-E811-A49A-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/82AC42E2-9559-E811-B598-FA163EA37F92.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/84DCF36C-8759-E811-8D58-FA163E0286FE.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/868E5062-1C5A-E811-BC8E-FA163EFB69E3.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/888EEB66-1B5A-E811-AF49-FA163E162D4E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/8CAF4C08-E559-E811-A35D-FA163EFD98DC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/904EDD4D-2A5A-E811-ADF1-02163E019F9E.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/9896654B-D759-E811-9C9B-FA163EB32A35.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/9A8BC05F-A859-E811-B714-FA163E6EBE8A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/9C8C9615-A159-E811-A2BE-FA163E54D0D4.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/A2FB168D-CF59-E811-915C-FA163E57B050.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/A46C1E03-B259-E811-9654-FA163E8CA0FA.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/A4EBEA18-A159-E811-8221-FA163E73F7A2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/A8F0066F-1B5A-E811-AD78-FA163E718491.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/ACEBAADE-9559-E811-853B-FA163E6B64D8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/B2693A1A-A159-E811-8B45-FA163E8385EB.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/B8444B57-9A59-E811-A373-FA163EB534AC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/BA2E9606-185A-E811-9437-FA163E49583C.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/BA9AF7FA-0F5A-E811-905E-FA163E587A6B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/BEAF74CD-B159-E811-8D54-FA163EF4B138.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/C8014898-B259-E811-8DC9-FA163EFC49F9.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/CAEE6879-1B5A-E811-A64C-FA163EF2B2D3.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/CC2C6C28-BB59-E811-A79F-FA163EB863FF.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/D0F8B9E7-0F5A-E811-8E4E-FA163EFB69E3.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/D0FDAB86-CF59-E811-A23B-FA163E6009F5.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/D8BF8092-155A-E811-A27C-FA163EC01FA8.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/DC9804E6-B159-E811-BBA1-FA163EB863FF.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/E202BA88-A859-E811-8193-FA163EC49E1F.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/E48FD84D-9A59-E811-A486-FA163E8AA6FB.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/E6662768-1B5A-E811-A6BF-FA163E7DCA90.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/EA1FE6A7-7959-E811-A794-FA163E4BB6D2.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/EAB80BED-155A-E811-A332-FA163EFB69E3.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/EEB45549-C559-E811-820E-FA163EAD67BC.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/F0334F6E-1B5A-E811-ACBE-FA163E587A6B.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/F0494FE8-9559-E811-8F9F-FA163E014C20.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/F0AF3A4C-9A59-E811-9ED9-FA163E1CAB16.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/F4027D34-A559-E811-8595-FA163EE8C9C6.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/F4078957-165A-E811-9279-FA163E718491.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/F665CBFE-B859-E811-AB00-FA163E52FDA7.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/FA35046E-C959-E811-BFAA-FA163E7DED4A.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/FCBEE91B-A159-E811-B310-FA163E954B62.root',
       '/store/mc/RunIIFall17MiniAODv2/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/60000/FE3E9672-1B5A-E811-B3C4-FA163E49583C.root',
] )
