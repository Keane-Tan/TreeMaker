import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/02FC4DC3-7B8F-E811-B533-0025904C6226.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/08011F29-1F91-E811-A04F-0025905C42A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/08FFA041-F18F-E811-8BC1-0025905C96A6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/0A599EA3-4A8F-E811-B5EA-0025905C3DF8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/0AB7F68B-BA8F-E811-922C-0025904C6568.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/0AE12704-BA8F-E811-95A6-0025904E9010.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/0CBD68AC-618F-E811-8B38-0025905C94D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/104B9974-A98F-E811-90C7-0CC47AFB7D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/10EFCA33-1391-E811-A418-0025904CDDFA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/12896507-BA8F-E811-96E2-0025905D1CAC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/188E55F6-B18F-E811-A9AF-0025905C54B8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/1A8C02F4-B18F-E811-A4BB-0025905C54FE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/1C6C89E0-7F8F-E811-A2F5-0025904C6622.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/1E29A0F3-878F-E811-9BA2-0CC47AFB80DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/244B148B-6790-E811-B2AA-0025905C43EA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/246EF9A5-1191-E811-AC40-0025905C4300.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/2C14D719-C88F-E811-A9CB-0CC47AF9B2C6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/2C34B6EF-B18F-E811-9CC1-0025905C54C6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/2CB27509-BA8F-E811-A06B-0025904C516E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/2CE0F208-BA8F-E811-8346-0025905D1CB2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/2E9030DB-7F8F-E811-8999-0025905C54C4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/3055E5DC-7F8F-E811-A404-0CC47AFB7D48.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/34064626-1F91-E811-B9FD-0025904C51DA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/344B92F4-988F-E811-A3E4-0025904C6378.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/3AECD6FD-E890-E811-BF9A-0CC47AFB7D88.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/3C5066A3-1191-E811-BC65-0025904C66EC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/3E396474-A98F-E811-B68B-0CC47AFB7D48.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/3EB2E103-BA8F-E811-964F-0025905C2CE8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/40C77B3C-538F-E811-8018-0025905C5488.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/44521B1E-A28F-E811-88FA-0025905C975C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/44EC801B-C88F-E811-A557-0025905C53A4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/46F8D275-A98F-E811-8CB3-0CC47AF9B2C6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/4891E918-C88F-E811-AC14-0CC47AF9B2C2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/528834F7-B18F-E811-8342-0CC47AFB7D7C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/561F1075-A98F-E811-AB84-0CC47AF9B496.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/56BD72F2-0B91-E811-AE2B-0025904CDDEC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/58709202-888F-E811-825C-0025905D1D7A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/58797034-1391-E811-8514-0025905C42A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/5A5F4BF2-B18F-E811-A139-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/5CC92B07-BA8F-E811-B18A-0025904C516E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/601FC481-D390-E811-B89B-0CC47AF9B2BE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/603F8E2E-A28F-E811-BA8D-0CC47AFB7CEC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/62230757-1991-E811-9010-0025905C53D0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/6443CAE4-7F8F-E811-A960-0025904C66A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/6A5DE153-1991-E811-AE0A-0025905C543A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/6A9480E1-7F8F-E811-9F35-0025905C3D3E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/6E11D706-BA8F-E811-9651-0025904C66A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/6E8773F2-B18F-E811-93A4-0CC47AFB7D88.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/74821CFD-988F-E811-BE13-0CC47AF9B2B6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/74E9B0A5-1191-E811-9459-0025904CF712.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/761E20C6-A18F-E811-8AA7-0025905C3E68.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/76658BAF-A18F-E811-B884-0CC47AF9B2C2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/7A5CB6C3-7B8F-E811-AAA0-0025905C43EC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/7AEC5377-A98F-E811-8D5E-0025904C4E2A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/7ED53862-3D8F-E811-9887-0025905C2CBE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/826E38DD-7F8F-E811-A0C5-0025904C6414.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/844F8BF7-988F-E811-A1F9-0CC47AFB7D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/84CEA31E-998F-E811-B700-0CC47AFB7DCC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/860A171D-998F-E811-B2FB-0025905C53B0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/8A9E87F6-B18F-E811-889C-0025905C542C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/8AF9A626-1F91-E811-A776-0025905C54DA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/8C444B7A-A98F-E811-891A-0CC47AFB7D7C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/8EDD4E57-7D90-E811-8F84-0025905C5500.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/90818D74-A98F-E811-A5AE-0CC47AFB7D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/90A89EC6-A18F-E811-8F6E-0CC47AF9B1B2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/90D189C4-7B8F-E811-918E-0025905C5432.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/9601E5F4-878F-E811-85C0-0CC47AF9B2EA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/96266D5A-1991-E811-8845-0025905C53DA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/96566774-A98F-E811-B30E-0025904CDDEC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/98147944-538F-E811-AAC9-0CC47AFB8104.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/98D47713-A28F-E811-94AB-0025904C66A6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/9A0EC474-A98F-E811-BB81-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/9A6A22F8-988F-E811-AE1A-0CC47AFB7D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/9AF12DC4-7B8F-E811-8A54-0025904E9010.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/9C78DC56-1991-E811-BCAB-0CC47AF9B1AE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/A2E6E4DE-7F8F-E811-83C5-0025904C66E4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/A6A35B21-6F8F-E811-83A1-0025904C4F9E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/A6A98AAE-618F-E811-A70E-0025905C54B8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/A6AD3988-438F-E811-AEA8-0CC47AF9B2C6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/A8C41D59-1991-E811-81D2-0025905C2CD2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/AA4731C1-A18F-E811-A98C-0CC47AFB7D7C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/AC091BE0-7F8F-E811-9089-0025904C669E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/ACA3A65C-2791-E811-AE61-0025905C975C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/AE1BA61D-998F-E811-90A3-0025904C6508.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/B28F1154-1991-E811-8C1D-0025905C94D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/B440C6F5-B18F-E811-853A-0025905D1D62.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/B460C6A6-1191-E811-BD5C-0025905C42F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/B4E524F2-B18F-E811-AE9E-0025905D1E0A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/B6EADE75-A98F-E811-8D49-0CC47AFB80E4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BAAFA63B-538F-E811-A174-0025904C51F2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BC13BE3F-A48F-E811-8B7D-0025905C3E68.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BC8C0E33-1391-E811-B0DE-0025905C5432.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BCCC35F4-878F-E811-9E13-0025904CF75A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BE2C28CA-7B8F-E811-8C7B-0025905C3E68.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BE2D0EFD-988F-E811-A6BB-0CC47AFB81B4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BE5071E0-7F8F-E811-9FC4-0025905C95F8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BE789A31-1391-E811-8436-0025905C54B8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BE939C75-A98F-E811-BC4B-0025905C54F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/BEC2F074-A98F-E811-9778-0025905C96A4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/C0A53CA3-4A8F-E811-86BC-0CC47AF9B2C6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/C0B01138-998F-E811-955A-0025905D1CB4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/C66D355F-688F-E811-8241-0025905C42A8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/C69B7B25-6F8F-E811-9CD9-0025905C54C6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/C6D4A630-6E8F-E811-9583-0025904C4F9C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/CAC7BA06-BA8F-E811-A4A6-0025904C66A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/CC2804AC-4A8F-E811-956C-0025905C542C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/CC30FF42-D38F-E811-A293-0CC47AFB80DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/D02069C4-7B8F-E811-A469-0025905C3D98.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/D45BF406-BA8F-E811-9189-0025904C66A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/D6F2F401-B28F-E811-B5EF-0CC47AF9B1D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/DA7A8820-6F8F-E811-AB3D-0CC47AF9B2F2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/DC6BEC85-588F-E811-A11F-0CC47AFB7D7C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/E02CD8DF-7F8F-E811-A3C5-0025905C2CD0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/E4367B3B-6E8F-E811-8C95-0CC47AF9B2CE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/E6375D8C-BA8F-E811-BDD9-0025904CF710.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/E8E2615A-688F-E811-B587-003048947BB9.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/EC1ECB00-A58F-E811-B5CA-0025904C637A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/EE9A2A8B-BA8F-E811-BC2E-0025904CF93C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F0142732-6E8F-E811-BED4-0025904C4F9C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F02C79F4-878F-E811-AA23-0CC47AF9B13A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F48F7315-6F8F-E811-9E90-0CC47AF9B2BA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F4C8E455-1991-E811-A8EF-0025905D1D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F6FD42DE-7F8F-E811-8E59-0025905C9724.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F849E738-1391-E811-9907-0025905C54D8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/F8B5BB59-688F-E811-8556-0025905BA736.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/FA8364F3-878F-E811-B464-0CC47AFB80F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/FAC5FBEF-B18F-E811-B857-0025904C4E2A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/FC8D2607-BA8F-E811-AB49-0025904C516E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/FEC3F6C9-7B8F-E811-9984-0025905D1D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/00000/FEF878A3-1191-E811-A7C1-0025904C66A4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/044A864C-A68F-E811-863B-0CC47AFB80E4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/04C7A814-1B90-E811-8DBC-0025905C53D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/0E9A711E-1B90-E811-9749-0025905D1D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/10439084-0990-E811-8361-0025905D1D00.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/146E98FF-D98F-E811-AF59-0025904C516C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/1606F319-7B8F-E811-B06B-0CC47AF9B302.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/185D3DB0-F58F-E811-BEC7-0025905C2CBC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/1C4E4851-A08F-E811-86AD-0025905C53A6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/1E63FC71-7D8F-E811-9802-0025905C54D8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/1EB82231-AC8F-E811-88B5-0025905C5432.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/24D59760-948F-E811-BE09-0025905C54FC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/280253F2-988F-E811-AD07-0025905C542E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/2E6398D0-D68F-E811-8245-0CC47AFB7D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/2E923484-0790-E811-B88A-0025905C53D0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/3065AA7A-0790-E811-8BE4-0CC47AFB7DCC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/32267C26-E58F-E811-8D79-0025905C2CE4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/32D0273D-C98F-E811-8ABC-0025905C4300.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/34EC477D-2290-E811-A29F-0025904C637C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/367ED215-1B90-E811-846F-0025905C2CE4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/387BA33B-1190-E811-A90D-0025905D1D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/38F3D9BC-F58F-E811-9B8A-0025905C96A4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/3A26EBFA-EE8F-E811-91D6-0025905C3D40.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/3ED9B7BD-0790-E811-8E9C-0025905C54FC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/42F5BEB9-0790-E811-B26D-0025905C54B8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/462BF583-0990-E811-9FF1-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/4C0FB706-EF8F-E811-8BDD-0025905C431C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/5212A64F-818F-E811-9E85-0025905D1E0A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/587AEE4B-A68F-E811-B032-0025904C66F6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/669E6CAD-0790-E811-B23E-0025905C54F6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/68F023DA-D98F-E811-B99C-0025905C53DA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/6AEFB572-F98F-E811-A218-0025905C5430.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/6E405E3F-1190-E811-A3A8-0025904C6414.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/6EF1C1D0-F28F-E811-8E99-0CC47AF9B32A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/6EFCF81A-7B8F-E811-AAAD-0CC47AF9B2E6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/747EA532-AC8F-E811-B538-0025905C96E8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/7ACF19E7-8B8F-E811-80A9-0CC47AF9B2D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/7EE34AFE-EE8F-E811-BE75-0CC47AFB80E4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/80AFB8CD-0A91-E811-83A7-0CC47AFB80DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/82B8FA43-FD8F-E811-9809-0025905C2CD2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/82EF62D0-D68F-E811-8D0A-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/8CDF123E-C98F-E811-BA4C-0025905C5430.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/90C00F76-7D8F-E811-A671-0CC47AFB7CEC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/9288A5EE-8B8F-E811-888E-0025905C53F0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/942D8C53-BC8F-E811-A7B1-0CC47AF9B496.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/9ECC2371-F98F-E811-A16F-0025905C2CD2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/A6364DD2-F28F-E811-9849-0025905C2CBC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/AA65623E-1190-E811-AA55-0025905D1E00.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/AA95714F-BC8F-E811-9EEF-0025904C5180.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/B2DCC7B5-A68F-E811-977B-0CC47AFB7D60.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/B47AF742-818F-E811-A480-0CC47AF9B2F2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/B8F237FB-D98F-E811-BCEC-0025904CF102.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/BAC65B51-BC8F-E811-8D3D-0025904B7C26.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/BC3941E6-8B8F-E811-82AE-0CC47AF9B2FE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/BE1040E6-8B8F-E811-B316-0CC47AFB7D5C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C0572472-7D8F-E811-BDB0-0CC47AFB81BC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C080A24E-818F-E811-BB1B-0025905C53D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C4761F72-7D8F-E811-8480-0CC47AF9B51A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C63A7055-E78F-E811-B377-0025905C3D6A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C6AFCDA1-EB8F-E811-A188-0025905C4300.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C6D1C6E6-8B8F-E811-8A60-0025904CF75A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C88E57AA-738F-E811-987B-0025905C53A8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/C89C3772-F98F-E811-8322-0025905C2D98.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/CE2C1337-E18F-E811-B151-0025904C66F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/CE8DF641-C98F-E811-B717-0025905C3E66.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/CE919A74-0790-E811-9EBF-0CC47AF9B2B6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/D0D5B716-7B8F-E811-9E89-0CC47AFB7DDC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/D2504E43-818F-E811-8AC0-0025905D1CB2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/D40439FD-EE8F-E811-AF4D-0025905D1CAE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/D4826CB3-DC8F-E811-A6D2-0025904CF102.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/D845EA42-818F-E811-8E4A-0CC47AF9B1D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/D8DC7B1B-7B8F-E811-8797-0CC47AF9B51A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/DE1EC44F-0A91-E811-A8AC-0CC47AFB80DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/E2C2AE65-9F8F-E811-91EA-0025905C53A6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/E49B6174-EE8F-E811-BCD6-0CC47AF9B2BE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/E63D72B3-F58F-E811-B199-0CC47AFB7DDC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/EEAD0ECF-F28F-E811-8171-0025904C4F9C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/F863F8B4-FE8F-E811-A447-0025905C42FE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/20000/FCE8BF74-0790-E811-B9F5-0CC47AF9B23A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/028E1938-8590-E811-9C7F-0025905D1E00.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/0465CF6E-B18F-E811-A4B0-0025905C4262.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/04C99136-878F-E811-8632-0CC47AFB7D48.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/0A7F8471-B18F-E811-AB60-0025905BA736.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/0C6DF5A1-708F-E811-B9C8-0CC47AFB7CEC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/10E52771-B18F-E811-B8B4-0CC47AFB7DDC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/12041132-878F-E811-A920-0025905C54F6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/145D6711-928F-E811-9554-0025904C4F9C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/14F9F533-8590-E811-ABD9-0025905C54C4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/16774F85-658F-E811-BB84-0025904C637C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/169AEFEF-788F-E811-BB50-0025905C3E68.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/184B8B6D-B18F-E811-82F4-0025905D1D02.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/18E4D684-658F-E811-825D-0025905D1D78.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/201A70EF-788F-E811-AD7B-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/205327FD-C58F-E811-B849-0CC47AF9B2D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/20E45773-B18F-E811-AE52-0025905C4300.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/22B7AC33-8590-E811-BE3C-0025905C96A4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/24C8EDF1-788F-E811-9150-0CC47AFB80E4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/24CA1D35-8590-E811-AF98-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/2887492E-878F-E811-A517-0025905C54D8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/2E0E31AA-A490-E811-BC7B-0025905C54FC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/3005F9F2-788F-E811-A35E-0CC47AFB80D4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/3090DCFF-C58F-E811-BC0A-0025905C53AA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/32CB906E-B18F-E811-B35B-0025905C3E68.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/3686F072-B18F-E811-99DD-0CC47AF9B2E6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/4AC85F71-B18F-E811-A455-0025904C4E2A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/580C5AFC-C58F-E811-A0B3-0CC47AFB7D88.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/58F93FF4-788F-E811-B782-0025905C53F0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/5AAEF323-C08F-E811-AC53-0025905C96A4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/6834E1EE-788F-E811-939F-0CC47AF9B2D2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/688FA29E-708F-E811-A285-0025904C516C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/68BFC4FB-C58F-E811-B4CC-0CC47AFB7D88.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/68E32B33-8590-E811-864A-0025905C54F6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/6CF86D2C-878F-E811-AC0F-0025904C5DDA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/6E83FD33-8590-E811-9DCC-0025905C5486.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/70A2E557-B88F-E811-BAA6-0025905C54DA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/763D43A1-708F-E811-AF8E-0025905C94D0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/782D182D-878F-E811-83C9-0025904C5180.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/7A5A7655-B88F-E811-8BC7-0025905C42FE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/7C0D4683-658F-E811-9F04-0025905C2CD2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/7C58290F-928F-E811-AC3F-0025904B7C42.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/844B9E32-8590-E811-950E-0025905C9726.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/84C5B322-C08F-E811-B67F-0025904C516C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/84CEE2E9-CF8F-E811-A36E-0025905C53DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/8643BC38-8590-E811-A543-0025905C42A2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/92AA9032-8590-E811-9286-0025905D1CAE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/94A3B030-8590-E811-A30C-0025905C3D6A.root',
] )
readFiles.extend( [
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/9C4BA772-B18F-E811-8E98-0025905C54B8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/9CE49770-B18F-E811-8DA8-0025904E9012.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/A01194ED-CF8F-E811-AED3-0025905C54F6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/A0668631-8590-E811-BD36-0CC47AF9B302.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/A0A4A4EA-CF8F-E811-BF15-0CC47AFB7D48.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/A23EF1F7-C58F-E811-B5E6-0025905C53AA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/A2B4A890-5A8F-E811-82FC-0CC47AF9B1D6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/AA2F6A9F-708F-E811-B808-0025904C6620.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/ACBF8694-3B8F-E811-8C0A-0CC47AFB80F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/B69F4D72-B18F-E811-BA05-0025905C54F6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/B6C38EEE-CF8F-E811-80D4-0025905C9726.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/B8C8C11F-928F-E811-B187-0025904C5DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/BA22AA2C-878F-E811-B711-0025905D1D52.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/BCD6F5ED-788F-E811-948B-0025905D1E08.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/C054151F-928F-E811-9344-0025905C42F4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/C060DB30-8590-E811-B911-0025904C6224.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/C6A68F23-C08F-E811-A526-0CC47AFB7D5C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/C8E67672-B18F-E811-97C1-0025905C3DD8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/CADFB27A-8590-E811-9CA0-0025905C3D3E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/D46D2A34-8590-E811-A9A3-0025904B9B3E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/D4925572-B18F-E811-8CF1-0CC47AF9B2F2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/D6BC27D9-7D90-E811-AADC-0CC47AF9B23A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/D8B6A770-B18F-E811-B050-0025905C2CD2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/F0FC1A2F-8590-E811-860A-0025905C5430.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/F815A4EA-CF8F-E811-B541-0CC47AFB7D90.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/40000/FEE89B31-8590-E811-B93A-0025904C4F9C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/009DC5FC-FD8F-E811-B407-0025905C3E38.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/1CDE59D7-2290-E811-9E33-0025905C542C.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/285D28B1-958F-E811-8FA1-0CC47AF9B496.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/28DBF256-0690-E811-B031-0025904C68DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/364D6BFE-1A90-E811-B9E2-0025905C9740.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/3876362A-1C90-E811-8759-0025905C3E66.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/3C622CC7-2F90-E811-9262-0025905BA734.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/484CD817-C58F-E811-B223-0025905C53DC.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/58D86F63-0E90-E811-A834-0CC47AF9B306.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/5A80D3C7-2890-E811-A9C2-0025904C67B4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/5E845E4E-978F-E811-A959-0025905D1E0A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/60DC01D9-2290-E811-9F84-0025905D1D78.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/64E0BDF5-C48F-E811-AFC1-0CC47AF9B2C2.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/6664B8F3-8C8F-E811-A4CD-0CC47AF9B1EA.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/724847E8-878F-E811-9394-0CC47AF9B51A.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/886D9823-988F-E811-8A2F-0025904C6416.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/8C05E0A6-2B90-E811-BE3C-0025905C975E.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/926EFA9A-2B90-E811-B272-0025905C9724.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/9EB31B03-C58F-E811-A800-0025904C6624.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/ACEF5EFC-1A90-E811-8470-0CC47AF9B2CE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/B6A5F1C3-2890-E811-A103-0025905C96A6.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/BA5FC8FB-1F90-E811-A96A-0025904C66E8.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/C03E9A1C-7B8F-E811-A441-0025905C5484.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/C48E3397-1290-E811-A34A-0CC47AF9B2CE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/C61BD8C5-2890-E811-800C-0025904C66E4.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/D8C7B9C9-2F90-E811-9C46-0025905C53F0.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/E09BF618-1890-E811-8FD4-0CC47AF9B2CE.root',
       '/store/data/Run2016H/HTMHT/MINIAOD/17Jul2018-v1/50000/EA7FADF4-C48F-E811-AC86-0025904C641C.root',
] )
