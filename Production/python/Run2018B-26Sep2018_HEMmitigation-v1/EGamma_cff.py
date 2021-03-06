import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/0A4CD2EB-E926-9145-8DF6-B7996B011FEE.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/11ED117F-A1BC-404B-A22E-C7F0F0CB4887.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/15862D97-1977-8341-B6D3-4CF6F07C74D3.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/1DC7C616-34A9-164B-AF5F-D20410214C57.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/32A5B884-20B3-B542-A447-3433C649B5CC.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/38046344-BFEB-E542-97F4-1890904C3EEF.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/46C3D5F8-8EC8-AB46-A66C-5591659111AD.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/4B0F1FE7-1E84-8D49-BA9C-4C97C5DBDB1C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/4B5D3FED-0C1A-6D4E-884B-094B90A343C9.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/4BFDDDE8-9BA5-454C-9060-E393B636F3A2.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/52CE80FD-8592-3749-8101-B1648897165C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/53C74AFE-8387-0243-BA15-E98CEE5B578B.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/578341A0-4D03-0B4B-806E-9C94A96263CD.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/65A846C0-DAEF-3B42-90C6-FE316435BC24.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/677D6E4F-E737-6B47-B607-BBC639E9C741.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/692F24BF-6CC3-E04B-8050-1D92F35E5798.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/750D66C8-30B4-434E-B8D6-237AAB9D3E71.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/77FC313D-8706-6A45-98A3-0A0544E76E13.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/7B21A3C2-E1CB-824F-852C-DC8F268CA78A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/7CA6CB78-C754-6941-9E62-55FE706FEA2C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/837390C5-1851-0E4F-9FBB-F7F0F08904EA.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/8A611A38-8EF2-044A-AC4A-D86765547379.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/92BA5D9C-C36D-0847-A120-8F1446B5FC85.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/962A87F6-7842-C04C-99AB-593B957A1552.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/9BDF7BC9-BE47-C74B-9144-387D89BAB709.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/9E10B638-4284-7C40-B898-D28BAA734B3C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A23B5826-5A50-864C-8D52-27A9D621413E.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A2B9D2DB-8A73-5D4C-9E8B-25F7BDE55B1D.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A2F38180-B9B1-344B-8E3B-F93CC71B345E.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A3026B2B-726D-3E4A-91BA-129E13650EBF.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A43BB925-69FB-B944-BB7B-42EB33375199.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A43E1018-F590-4D43-B463-AB4649A62B10.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/A4C914AC-F00F-B24D-B40B-8C8E4B702110.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/AD445391-9C6B-7B4D-977E-63E9C4B49C6D.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/AD858AA4-E01F-5849-8444-1D2DAC8FA739.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/B07EAD88-F3C3-9549-8CFF-2735A371D04A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/B932C8FF-4C7B-5947-BFCE-2FDB750185CB.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/CB6C514C-DB87-BD46-998E-472EC3897583.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/D1415E4B-7A33-B347-B734-9040B3B623F1.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/DE8121A6-E8E3-1043-A749-3F0567AD210B.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/E8E5940A-0F8B-E948-B079-3F3D9E9F3C46.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/E9493154-AAEE-7E49-BE80-E00C4D95EA56.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/F353005E-6F50-0444-8E76-5891F69F403A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/FB6CF0A7-A4EE-5842-AFAC-5AC1080A94F4.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/100000/FFAF347A-464B-1547-8812-A6187BF2D5FB.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/4D507D40-98B6-944E-B8F8-65EFFCF87A0A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/4D5B612A-4F04-FA41-AB33-E448DE996C2C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/4D6F720D-97CD-894E-B71C-32D81FD9D7FF.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/73F8FC68-F04F-6542-A158-6A5A01FB9BFD.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/862060DA-0FD8-C444-95C6-9CCB1A51F027.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/905D3E60-DABE-8C4C-959D-818C55FC7D0A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/9C8771F3-4AFA-E14E-BB95-3D12B382D833.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/A859C532-A659-1B47-9C98-82EA080D6B1E.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/B7AABCB8-04EE-AD45-9EF4-06CC1451A4B6.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/C280C298-4549-234F-8F28-5C631E68DBA2.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/DAB54E09-ACBA-9F46-B529-192B17E2C6E4.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/EEB9A584-8C5A-1A45-B046-D7C9A06082B5.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/FA540A4D-41A3-CD48-9568-9AE186114782.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/FF3810BB-A83B-054F-9FEE-D6146B599056.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/110000/FFE3BBFA-A848-1146-9632-5206DBE4620A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/03BE06A0-3A42-524D-A32F-F4A8A534DD9B.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/18D2D78B-A847-C641-B972-73C7BA42BD98.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/1BCB0E73-D63D-CA43-97AC-B9B000D3B87C.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/1E4EA41A-D702-C847-9A19-B6B46C9DA9CB.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/21E2AE3F-1F40-924F-A1CD-BC0B3424E2DF.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/2762A7E6-0EC5-FA45-9A36-D813A3CAA294.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/3096F7A3-820F-DE48-B222-4FEB656E40AE.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/385FBD07-4041-4D41-B1BE-87CC20FE38BF.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/38F1A7C8-8FA9-724A-A72B-34BC31D6AD2A.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/54C86399-B8BA-B74D-BAEC-27B5C3B52397.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/55075BCD-7978-F141-9202-C4667A19D1BB.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/57308E6F-7D50-A746-8D97-B5ABEF9F5F93.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/5824058F-72C4-6644-B1B6-B4B0BB16FDBB.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/63E7DE76-1729-484A-B3D9-52410E370091.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/64ADAE30-9867-DE48-BF06-31DAC66F5CE1.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/6E7AA956-A6B7-8242-A50D-C032F999893B.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/705EE39A-4F8A-5043-B911-ACB6B5F932EA.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/73439E50-AFB7-0F45-BB0C-9020F90B6774.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/752650BF-2A13-F946-BC82-3E4D98E28BC0.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/79ABCBAF-7DEF-0842-B260-D15DC0CE9D87.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/821B9568-A0FF-2E42-B5CE-795ADEC1C2F2.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/85E919FE-5D7F-2949-97A5-F9F6948EF321.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/9CFAC8D7-2BEC-AD44-8F7B-1AECA2C39B2F.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/AF558E70-2E46-C642-8D2B-E10D0D8F8C68.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/BB41E4ED-4460-F54B-B2FB-D05D66ED04AE.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/C1F03B49-068F-0946-ADD9-8B7BFB9A2B54.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/C36DA34E-B59E-744A-B51F-E4150AD7EB40.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/DC11A25A-D651-F847-B37C-D408B80F1CC1.root',
       '/store/data/Run2018B/EGamma/MINIAOD/26Sep2018_HEMmitigation-v1/270000/FF6827A2-63B6-954D-BFF1-E49349412DCD.root',
] )
