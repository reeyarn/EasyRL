Q: I tried to unzip the US GAAP 2020 XBRL taxonomy and got so many files. help me understand the structure and content: 


```
ls -R us-gaap-2020-01-31 
dis dqcrules elts entire META-INF stm
 
us-gaap-2020-01-31/dis:
us-gaap-dis-acec-2020-01-31.xsd us-gaap-dis-ides-cal-2020-01-31.xml us-gaap-dis-rbtmp05-pre-2020-01-31.xml
us-gaap-dis-acec-def-2020-01-31.xml us-gaap-dis-ides-def-2020-01-31.xml us-gaap-dis-rbtmp06-2020-01-31.xsd
us-gaap-dis-acec-pre-2020-01-31.xml us-gaap-dis-ides-pre-2020-01-31.xml us-gaap-dis-rbtmp06-cal-2020-01-31.xml
us-gaap-dis-ap-2020-01-31.xsd us-gaap-dis-ides1-cal-2020-01-31.xml us-gaap-dis-rbtmp06-def-2020-01-31.xml
us-gaap-dis-ap-def-2020-01-31.xml us-gaap-dis-idestmp011-2020-01-31.xsd us-gaap-dis-rbtmp06-pre-2020-01-31.xml
us-gaap-dis-ap-pre-2020-01-31.xml us-gaap-dis-idestmp011-cal-2020-01-31.xml us-gaap-dis-rbtmp07-2020-01-31.xsd
us-gaap-dis-aro-2020-01-31.xsd us-gaap-dis-idestmp011-def-2020-01-31.xml us-gaap-dis-rbtmp07-cal-2020-01-31.xml
us-gaap-dis-aro-pre-2020-01-31.xml us-gaap-dis-idestmp011-pre-2020-01-31.xml us-gaap-dis-rbtmp07-def-2020-01-31.xml
us-gaap-dis-bc-2020-01-31.xsd us-gaap-dis-idestmp012-2020-01-31.xsd us-gaap-dis-rbtmp07-pre-2020-01-31.xml
us-gaap-dis-bc-cal-2020-01-31.xml us-gaap-dis-idestmp012-cal-2020-01-31.xml us-gaap-dis-rbtmp08-2020-01-31.xsd
us-gaap-dis-bc-def-2020-01-31.xml us-gaap-dis-idestmp012-def-2020-01-31.xml us-gaap-dis-rbtmp08-cal-2020-01-31.xml
us-gaap-dis-bc-pre-2020-01-31.xml us-gaap-dis-idestmp012-pre-2020-01-31.xml us-gaap-dis-rbtmp08-def-2020-01-31.xml
us-gaap-dis-bsoff-2020-01-31.xsd us-gaap-dis-idestmp021-2020-01-31.xsd us-gaap-dis-rbtmp08-pre-2020-01-31.xml
us-gaap-dis-bsoff-cal-2020-01-31.xml us-gaap-dis-idestmp021-cal-2020-01-31.xml us-gaap-dis-rbtmp09-2020-01-31.xsd
us-gaap-dis-bsoff-def-2020-01-31.xml us-gaap-dis-idestmp021-def-2020-01-31.xml us-gaap-dis-rbtmp09-cal-2020-01-31.xml
us-gaap-dis-bsoff-pre-2020-01-31.xml us-gaap-dis-idestmp021-pre-2020-01-31.xml us-gaap-dis-rbtmp09-def-2020-01-31.xml
us-gaap-dis-bsoff1-cal-2020-01-31.xml us-gaap-dis-idestmp022-2020-01-31.xsd us-gaap-dis-rbtmp09-pre-2020-01-31.xml
us-gaap-dis-cc-2020-01-31.xsd us-gaap-dis-idestmp022-cal-2020-01-31.xml us-gaap-dis-rbtmp101-2020-01-31.xsd
us-gaap-dis-cc-cal-2020-01-31.xml us-gaap-dis-idestmp022-def-2020-01-31.xml us-gaap-dis-rbtmp101-pre-2020-01-31.xml
us-gaap-dis-cc-def-2020-01-31.xml us-gaap-dis-idestmp022-pre-2020-01-31.xml us-gaap-dis-rbtmp102-2020-01-31.xsd
us-gaap-dis-cc-pre-2020-01-31.xml us-gaap-dis-idestmp03-2020-01-31.xsd us-gaap-dis-rbtmp102-def-2020-01-31.xml
us-gaap-dis-cc2-cal-2020-01-31.xml us-gaap-dis-idestmp03-cal-2020-01-31.xml us-gaap-dis-rbtmp102-pre-2020-01-31.xml
us-gaap-dis-cce-2020-01-31.xsd us-gaap-dis-idestmp03-pre-2020-01-31.xml us-gaap-dis-rbtmp103-2020-01-31.xsd
us-gaap-dis-cce-def-2020-01-31.xml us-gaap-dis-idestmp04-2020-01-31.xsd us-gaap-dis-rbtmp103-def-2020-01-31.xml
us-gaap-dis-cce-pre-2020-01-31.xml us-gaap-dis-idestmp04-cal-2020-01-31.xml us-gaap-dis-rbtmp103-pre-2020-01-31.xml
us-gaap-dis-cecl-2020-01-31.xsd us-gaap-dis-idestmp04-pre-2020-01-31.xml us-gaap-dis-rbtmp104-2020-01-31.xsd
us-gaap-dis-cecl-cal-2020-01-31.xml us-gaap-dis-inctax-2020-01-31.xsd us-gaap-dis-rbtmp104-def-2020-01-31.xml
us-gaap-dis-cecl-def-2020-01-31.xml us-gaap-dis-inctax-cal-2020-01-31.xml us-gaap-dis-rbtmp104-pre-2020-01-31.xml
us-gaap-dis-cecl-pre-2020-01-31.xml us-gaap-dis-inctax-def-2020-01-31.xml us-gaap-dis-rbtmp105-2020-01-31.xsd
us-gaap-dis-ceclcalc2-2020-01-31.xsd us-gaap-dis-inctax-pre-2020-01-31.xml us-gaap-dis-rbtmp105-def-2020-01-31.xml
us-gaap-dis-ceclcalc2-cal-2020-01-31.xml us-gaap-dis-insldtmp01-2020-01-31.xsd us-gaap-dis-rbtmp105-pre-2020-01-31.xml
us-gaap-dis-ceclcalc3l-2020-01-31.xsd us-gaap-dis-insldtmp01-def-2020-01-31.xml us-gaap-dis-rbtmp111-2020-01-31.xsd
us-gaap-dis-ceclcalc3l-cal-2020-01-31.xml us-gaap-dis-insldtmp01-pre-2020-01-31.xml us-gaap-dis-rbtmp111-def-2020-01-31.xml
us-gaap-dis-cecltmp01-2020-01-31.xsd us-gaap-dis-insldtmp021-2020-01-31.xsd us-gaap-dis-rbtmp111-pre-2020-01-31.xml
us-gaap-dis-cecltmp01-cal-2020-01-31.xml us-gaap-dis-insldtmp021-cal-2020-01-31.xml us-gaap-dis-rbtmp112-2020-01-31.xsd
us-gaap-dis-cecltmp01-def-2020-01-31.xml us-gaap-dis-insldtmp021-def-2020-01-31.xml us-gaap-dis-rbtmp112-def-2020-01-31.xml
us-gaap-dis-cecltmp01-pre-2020-01-31.xml us-gaap-dis-insldtmp021-pre-2020-01-31.xml us-gaap-dis-rbtmp112-pre-2020-01-31.xml
us-gaap-dis-cecltmp02-2020-01-31.xsd us-gaap-dis-insldtmp022-2020-01-31.xsd us-gaap-dis-rbtmp113-2020-01-31.xsd
us-gaap-dis-cecltmp02-cal-2020-01-31.xml us-gaap-dis-insldtmp022-def-2020-01-31.xml us-gaap-dis-rbtmp113-pre-2020-01-31.xml
us-gaap-dis-cecltmp02-def-2020-01-31.xml us-gaap-dis-insldtmp022-pre-2020-01-31.xml us-gaap-dis-rbtmp121-2020-01-31.xsd
us-gaap-dis-cecltmp02-pre-2020-01-31.xml us-gaap-dis-insldtmp023-2020-01-31.xsd us-gaap-dis-rbtmp121-def-2020-01-31.xml
us-gaap-dis-cecltmp03-2020-01-31.xsd us-gaap-dis-insldtmp023-def-2020-01-31.xml us-gaap-dis-rbtmp121-pre-2020-01-31.xml
us-gaap-dis-cecltmp03-def-2020-01-31.xml us-gaap-dis-insldtmp023-pre-2020-01-31.xml us-gaap-dis-rbtmp122-2020-01-31.xsd
us-gaap-dis-cecltmp03-pre-2020-01-31.xml us-gaap-dis-insldtmp024-2020-01-31.xsd us-gaap-dis-rbtmp122-def-2020-01-31.xml
us-gaap-dis-cecltmp04-2020-01-31.xsd us-gaap-dis-insldtmp024-def-2020-01-31.xml us-gaap-dis-rbtmp122-pre-2020-01-31.xml
us-gaap-dis-cecltmp04-cal-2020-01-31.xml us-gaap-dis-insldtmp024-pre-2020-01-31.xml us-gaap-dis-rbtmp123-2020-01-31.xsd
us-gaap-dis-cecltmp04-def-2020-01-31.xml us-gaap-dis-insldtmp025-2020-01-31.xsd us-gaap-dis-rbtmp123-def-2020-01-31.xml
us-gaap-dis-cecltmp04-pre-2020-01-31.xml us-gaap-dis-insldtmp025-def-2020-01-31.xml us-gaap-dis-rbtmp123-pre-2020-01-31.xml
us-gaap-dis-cecltmp05-2020-01-31.xsd us-gaap-dis-insldtmp025-pre-2020-01-31.xml us-gaap-dis-rbtmp124-2020-01-31.xsd
us-gaap-dis-cecltmp05-def-2020-01-31.xml us-gaap-dis-insldtmp031-2020-01-31.xsd us-gaap-dis-rbtmp124-pre-2020-01-31.xml
us-gaap-dis-cecltmp05-pre-2020-01-31.xml us-gaap-dis-insldtmp031-def-2020-01-31.xml us-gaap-dis-rbtmp125-2020-01-31.xsd
us-gaap-dis-con-2020-01-31.xsd us-gaap-dis-insldtmp031-pre-2020-01-31.xml us-gaap-dis-rbtmp125-def-2020-01-31.xml
us-gaap-dis-con-def-2020-01-31.xml us-gaap-dis-insldtmp032-2020-01-31.xsd us-gaap-dis-rbtmp125-pre-2020-01-31.xml
us-gaap-dis-con-pre-2020-01-31.xml us-gaap-dis-insldtmp032-def-2020-01-31.xml us-gaap-dis-rbtmp131-2020-01-31.xsd
us-gaap-dis-crcgen-2020-01-31.xsd us-gaap-dis-insldtmp032-pre-2020-01-31.xml us-gaap-dis-rbtmp131-def-2020-01-31.xml
us-gaap-dis-crcgen-def-2020-01-31.xml us-gaap-dis-insldtmp033-2020-01-31.xsd us-gaap-dis-rbtmp131-pre-2020-01-31.xml
us-gaap-dis-crcgen-pre-2020-01-31.xml us-gaap-dis-insldtmp033-def-2020-01-31.xml us-gaap-dis-rbtmp132-2020-01-31.xsd
us-gaap-dis-crcpb-2020-01-31.xsd us-gaap-dis-insldtmp033-pre-2020-01-31.xml us-gaap-dis-rbtmp132-pre-2020-01-31.xml
us-gaap-dis-crcpb-pre-2020-01-31.xml us-gaap-dis-insldtmp041-2020-01-31.xsd us-gaap-dis-rbtmp141-2020-01-31.xsd
us-gaap-dis-crcrb-2020-01-31.xsd us-gaap-dis-insldtmp041-cal-2020-01-31.xml us-gaap-dis-rbtmp141-def-2020-01-31.xml
us-gaap-dis-crcrb-cal-2020-01-31.xml us-gaap-dis-insldtmp041-def-2020-01-31.xml us-gaap-dis-rbtmp141-pre-2020-01-31.xml
us-gaap-dis-crcrb-def-2020-01-31.xml us-gaap-dis-insldtmp041-pre-2020-01-31.xml us-gaap-dis-rbtmp142-2020-01-31.xsd
us-gaap-dis-crcrb-pre-2020-01-31.xml us-gaap-dis-insldtmp042-2020-01-31.xsd us-gaap-dis-rbtmp142-pre-2020-01-31.xml
us-gaap-dis-crcsbp-2020-01-31.xsd us-gaap-dis-insldtmp042-cal-2020-01-31.xml us-gaap-dis-rcc-2020-01-31.xsd
us-gaap-dis-crcsbp-cal-2020-01-31.xml us-gaap-dis-insldtmp042-def-2020-01-31.xml us-gaap-dis-rcc-cal-2020-01-31.xml
us-gaap-dis-crcsbp-def-2020-01-31.xml us-gaap-dis-insldtmp042-pre-2020-01-31.xml us-gaap-dis-rcc-def-2020-01-31.xml
us-gaap-dis-crcsbp-pre-2020-01-31.xml us-gaap-dis-insldtmp051-2020-01-31.xsd us-gaap-dis-rcc-pre-2020-01-31.xml
us-gaap-dis-ctbl-2020-01-31.xsd us-gaap-dis-insldtmp051-def-2020-01-31.xml us-gaap-dis-rcctmp01-2020-01-31.xsd
us-gaap-dis-ctbl-pre-2020-01-31.xml us-gaap-dis-insldtmp051-pre-2020-01-31.xml us-gaap-dis-rcctmp01-def-2020-01-31.xml
us-gaap-dis-dccpoa-2020-01-31.xsd us-gaap-dis-insldtmp052-2020-01-31.xsd us-gaap-dis-rcctmp01-pre-2020-01-31.xml
us-gaap-dis-dccpoa-pre-2020-01-31.xml us-gaap-dis-insldtmp052-def-2020-01-31.xml us-gaap-dis-rcctmp02-2020-01-31.xsd
us-gaap-dis-debt-2020-01-31.xsd us-gaap-dis-insldtmp052-pre-2020-01-31.xml us-gaap-dis-rcctmp02-pre-2020-01-31.xml
us-gaap-dis-debt-cal-2020-01-31.xml us-gaap-dis-insldtmp061-2020-01-31.xsd us-gaap-dis-rcctmp03-2020-01-31.xsd
us-gaap-dis-debt-def-2020-01-31.xml us-gaap-dis-insldtmp061-def-2020-01-31.xml us-gaap-dis-rcctmp03-def-2020-01-31.xml
us-gaap-dis-debt-pre-2020-01-31.xml us-gaap-dis-insldtmp061-pre-2020-01-31.xml us-gaap-dis-rcctmp03-pre-2020-01-31.xml
us-gaap-dis-diha-2020-01-31.xsd us-gaap-dis-insldtmp062-2020-01-31.xsd us-gaap-dis-rcctmp04-2020-01-31.xsd
us-gaap-dis-diha-cal-2020-01-31.xml us-gaap-dis-insldtmp062-def-2020-01-31.xml us-gaap-dis-rcctmp04-cal-2020-01-31.xml
us-gaap-dis-diha-def-2020-01-31.xml us-gaap-dis-insldtmp062-pre-2020-01-31.xml us-gaap-dis-rcctmp04-def-2020-01-31.xml
us-gaap-dis-diha-pre-2020-01-31.xml us-gaap-dis-inv-2020-01-31.xsd us-gaap-dis-rcctmp04-pre-2020-01-31.xml
us-gaap-dis-disops-2020-01-31.xsd us-gaap-dis-inv-cal-2020-01-31.xml us-gaap-dis-rcctmp05-2020-01-31.xsd
us-gaap-dis-disops-def-2020-01-31.xml us-gaap-dis-inv-def-2020-01-31.xml us-gaap-dis-rcctmp05-def-2020-01-31.xml
us-gaap-dis-disops-pre-2020-01-31.xml us-gaap-dis-inv-pre-2020-01-31.xml us-gaap-dis-rcctmp05-pre-2020-01-31.xml
us-gaap-dis-dr-2020-01-31.xsd us-gaap-dis-invco-2020-01-31.xsd us-gaap-dis-rd-2020-01-31.xsd
us-gaap-dis-dr-cal-2020-01-31.xml us-gaap-dis-invco-cal-2020-01-31.xml us-gaap-dis-rd-def-2020-01-31.xml
us-gaap-dis-dr-pre-2020-01-31.xml us-gaap-dis-invco-def-2020-01-31.xml us-gaap-dis-rd-pre-2020-01-31.xml
us-gaap-dis-edco-2020-01-31.xsd us-gaap-dis-invco-pre-2020-01-31.xml us-gaap-dis-re-2020-01-31.xsd
us-gaap-dis-edco-def-2020-01-31.xml us-gaap-dis-ir-2020-01-31.xsd us-gaap-dis-re-cal-2020-01-31.xml
us-gaap-dis-edco-pre-2020-01-31.xml us-gaap-dis-ir-def-2020-01-31.xml us-gaap-dis-re-def-2020-01-31.xml
us-gaap-dis-ei-2020-01-31.xsd us-gaap-dis-ir-pre-2020-01-31.xml us-gaap-dis-re-pre-2020-01-31.xml
us-gaap-dis-ei-cal-2020-01-31.xml us-gaap-dis-lea-2020-01-31.xsd us-gaap-dis-regop-2020-01-31.xsd
us-gaap-dis-ei-def-2020-01-31.xml us-gaap-dis-lea-pre-2020-01-31.xml us-gaap-dis-regop-cal-2020-01-31.xml
us-gaap-dis-ei-pre-2020-01-31.xml us-gaap-dis-leas-2020-01-31.xsd us-gaap-dis-regop-def-2020-01-31.xml
us-gaap-dis-emjv-2020-01-31.xsd us-gaap-dis-leas-cal-2020-01-31.xml us-gaap-dis-regop-pre-2020-01-31.xml
us-gaap-dis-emjv-def-2020-01-31.xml us-gaap-dis-leas-def-2020-01-31.xml us-gaap-dis-reorg-2020-01-31.xsd
us-gaap-dis-emjv-pre-2020-01-31.xml us-gaap-dis-leas-pre-2020-01-31.xml us-gaap-dis-reorg-def-2020-01-31.xml
us-gaap-dis-eps-2020-01-31.xsd us-gaap-dis-leastmp01-2020-01-31.xsd us-gaap-dis-reorg-pre-2020-01-31.xml
us-gaap-dis-eps-def-2020-01-31.xml us-gaap-dis-leastmp01-cal-2020-01-31.xml us-gaap-dis-rlnro-2020-01-31.xsd
us-gaap-dis-eps-pre-2020-01-31.xml us-gaap-dis-leastmp01-pre-2020-01-31.xml us-gaap-dis-rlnro-cal-2020-01-31.xml
us-gaap-dis-equity-2020-01-31.xsd us-gaap-dis-leastmp02-2020-01-31.xsd us-gaap-dis-rlnro-def-2020-01-31.xml
us-gaap-dis-equity-cal-2020-01-31.xml us-gaap-dis-leastmp02-cal-2020-01-31.xml us-gaap-dis-rlnro-pre-2020-01-31.xml
us-gaap-dis-equity-def-2020-01-31.xml us-gaap-dis-leastmp02-pre-2020-01-31.xml us-gaap-dis-rpd-2020-01-31.xsd
us-gaap-dis-equity-pre-2020-01-31.xml us-gaap-dis-leastmp021-2020-01-31.xsd us-gaap-dis-rpd-def-2020-01-31.xml
us-gaap-dis-ero-2020-01-31.xsd us-gaap-dis-leastmp021-cal-2020-01-31.xml us-gaap-dis-rpd-pre-2020-01-31.xml
us-gaap-dis-ero-def-2020-01-31.xml us-gaap-dis-leastmp03-2020-01-31.xsd us-gaap-dis-ru-2020-01-31.xsd
us-gaap-dis-ero-pre-2020-01-31.xml us-gaap-dis-leastmp03-cal-2020-01-31.xml us-gaap-dis-ru-def-2020-01-31.xml
us-gaap-dis-eui-2020-01-31.xsd us-gaap-dis-leastmp03-pre-2020-01-31.xml us-gaap-dis-ru-pre-2020-01-31.xml
us-gaap-dis-eui-def-2020-01-31.xml us-gaap-dis-leastmp04-2020-01-31.xsd us-gaap-dis-schedoi-fednote-2020-01-31.xsd
us-gaap-dis-eui-pre-2020-01-31.xml us-gaap-dis-leastmp04-cal-2020-01-31.xml us-gaap-dis-schedoi-fednote-def-2020-01-31.xml
us-gaap-dis-fifvd-2020-01-31.xsd us-gaap-dis-leastmp04-pre-2020-01-31.xml us-gaap-dis-schedoi-fednote-pre-2020-01-31.xml
us-gaap-dis-fifvd-cal-2020-01-31.xml us-gaap-dis-leastmp05-2020-01-31.xsd us-gaap-dis-schedoi-hold-2020-01-31.xsd
us-gaap-dis-fifvd-def-2020-01-31.xml us-gaap-dis-leastmp05-cal-2020-01-31.xml us-gaap-dis-schedoi-hold-cal-2020-01-31.xml
us-gaap-dis-fifvd-pre-2020-01-31.xml us-gaap-dis-leastmp05-pre-2020-01-31.xml us-gaap-dis-schedoi-hold-def-2020-01-31.xml
us-gaap-dis-fifvdtmp01-2020-01-31.xsd us-gaap-dis-ni-2020-01-31.xsd us-gaap-dis-schedoi-hold-pre-2020-01-31.xml
us-gaap-dis-fifvdtmp01-cal-2020-01-31.xml us-gaap-dis-ni-cal-2020-01-31.xml us-gaap-dis-schedoi-iiaa-2020-01-31.xsd
us-gaap-dis-fifvdtmp01-def-2020-01-31.xml us-gaap-dis-ni-def-2020-01-31.xml us-gaap-dis-schedoi-iiaa-def-2020-01-31.xml
us-gaap-dis-fifvdtmp01-pre-2020-01-31.xml us-gaap-dis-ni-pre-2020-01-31.xml us-gaap-dis-schedoi-iiaa-pre-2020-01-31.xml
us-gaap-dis-fifvdtmp02-2020-01-31.xsd us-gaap-dis-nt-2020-01-31.xsd us-gaap-dis-schedoi-oocw-2020-01-31.xsd
us-gaap-dis-fifvdtmp02-def-2020-01-31.xml us-gaap-dis-nt-def-2020-01-31.xml us-gaap-dis-schedoi-oocw-def-2020-01-31.xml
us-gaap-dis-fifvdtmp02-pre-2020-01-31.xml us-gaap-dis-nt-pre-2020-01-31.xml us-gaap-dis-schedoi-oocw-pre-2020-01-31.xml
us-gaap-dis-foct-2020-01-31.xsd us-gaap-dis-ocpfs-2020-01-31.xsd us-gaap-dis-schedoi-otsh-2020-01-31.xsd
us-gaap-dis-foct-cal-2020-01-31.xml us-gaap-dis-ocpfs-cal-2020-01-31.xml us-gaap-dis-schedoi-otsh-def-2020-01-31.xml
us-gaap-dis-foct-def-2020-01-31.xml us-gaap-dis-ocpfs-def-2020-01-31.xml us-gaap-dis-schedoi-otsh-pre-2020-01-31.xml
us-gaap-dis-foct-pre-2020-01-31.xml us-gaap-dis-ocpfs-pre-2020-01-31.xml us-gaap-dis-schedoi-shorthold-2020-01-31.xsd
us-gaap-dis-fs-bd-2020-01-31.xsd us-gaap-dis-oi-2020-01-31.xsd us-gaap-dis-schedoi-shorthold-def-2020-01-31.xml
us-gaap-dis-fs-bd-cal-2020-01-31.xml us-gaap-dis-oi-cal-2020-01-31.xml us-gaap-dis-schedoi-shorthold-pre-2020-01-31.xml
us-gaap-dis-fs-bd-def-2020-01-31.xml us-gaap-dis-oi-def-2020-01-31.xml us-gaap-dis-schedoi-sumhold-2020-01-31.xsd
us-gaap-dis-fs-bd-pre-2020-01-31.xml us-gaap-dis-oi-pre-2020-01-31.xml us-gaap-dis-schedoi-sumhold-def-2020-01-31.xml
us-gaap-dis-fs-bd3-cal-2020-01-31.xml us-gaap-dis-otherexp-2020-01-31.xsd us-gaap-dis-schedoi-sumhold-pre-2020-01-31.xml
us-gaap-dis-fs-bt-2020-01-31.xsd us-gaap-dis-otherexp-pre-2020-01-31.xml us-gaap-dis-se-2020-01-31.xsd
us-gaap-dis-fs-bt-cal-2020-01-31.xml us-gaap-dis-othliab-2020-01-31.xsd us-gaap-dis-se-def-2020-01-31.xml
us-gaap-dis-fs-bt-def-2020-01-31.xml us-gaap-dis-othliab-def-2020-01-31.xml us-gaap-dis-se-pre-2020-01-31.xml
us-gaap-dis-fs-bt-pre-2020-01-31.xml us-gaap-dis-othliab-pre-2020-01-31.xml us-gaap-dis-sec-cndfir-2020-01-31.xsd
us-gaap-dis-fs-bt1-cal-2020-01-31.xml us-gaap-dis-othliab5-cal-2020-01-31.xml us-gaap-dis-sec-cndfir-def-2020-01-31.xml
us-gaap-dis-fs-fhlb-2020-01-31.xsd us-gaap-dis-pay-2020-01-31.xsd us-gaap-dis-sec-cndfir-pre-2020-01-31.xml
us-gaap-dis-fs-fhlb-cal-2020-01-31.xml us-gaap-dis-pay-pre-2020-01-31.xml us-gaap-dis-sec-mort-2020-01-31.xsd
us-gaap-dis-fs-fhlb-def-2020-01-31.xml us-gaap-dis-ppe-2020-01-31.xsd us-gaap-dis-sec-mort-def-2020-01-31.xml
us-gaap-dis-fs-fhlb-pre-2020-01-31.xml us-gaap-dis-ppe-def-2020-01-31.xml us-gaap-dis-sec-mort-pre-2020-01-31.xml
us-gaap-dis-fs-ins-2020-01-31.xsd us-gaap-dis-ppe-pre-2020-01-31.xml us-gaap-dis-sec-re-2020-01-31.xsd
us-gaap-dis-fs-ins-cal-2020-01-31.xml us-gaap-dis-rbtmp011-2020-01-31.xsd us-gaap-dis-sec-re-def-2020-01-31.xml
us-gaap-dis-fs-ins-def-2020-01-31.xml us-gaap-dis-rbtmp011-cal-2020-01-31.xml us-gaap-dis-sec-re-pre-2020-01-31.xml
us-gaap-dis-fs-ins-pre-2020-01-31.xml us-gaap-dis-rbtmp011-def-2020-01-31.xml us-gaap-dis-sec-reins-2020-01-31.xsd
us-gaap-dis-fs-insa-2020-01-31.xsd us-gaap-dis-rbtmp011-pre-2020-01-31.xml us-gaap-dis-sec-reins-def-2020-01-31.xml
us-gaap-dis-fs-insa-cal-2020-01-31.xml us-gaap-dis-rbtmp012-2020-01-31.xsd us-gaap-dis-sec-reins-pre-2020-01-31.xml
us-gaap-dis-fs-insa-def-2020-01-31.xml us-gaap-dis-rbtmp012-cal-2020-01-31.xml us-gaap-dis-sec-sum-2020-01-31.xsd
us-gaap-dis-fs-insa-pre-2020-01-31.xml us-gaap-dis-rbtmp012-def-2020-01-31.xml us-gaap-dis-sec-sum-def-2020-01-31.xml
us-gaap-dis-fs-insa1-cal-2020-01-31.xml us-gaap-dis-rbtmp012-pre-2020-01-31.xml us-gaap-dis-sec-sum-pre-2020-01-31.xml
us-gaap-dis-fs-interest-2020-01-31.xsd us-gaap-dis-rbtmp02-2020-01-31.xsd us-gaap-dis-sec-supins-2020-01-31.xsd
us-gaap-dis-fs-interest-cal-2020-01-31.xml us-gaap-dis-rbtmp02-cal-2020-01-31.xml us-gaap-dis-sec-supins-def-2020-01-31.xml
us-gaap-dis-fs-interest-pre-2020-01-31.xml us-gaap-dis-rbtmp02-def-2020-01-31.xml us-gaap-dis-sec-supins-pre-2020-01-31.xml
us-gaap-dis-fs-mort-2020-01-31.xsd us-gaap-dis-rbtmp02-pre-2020-01-31.xml us-gaap-dis-sec-suppc-2020-01-31.xsd
us-gaap-dis-fs-mort-def-2020-01-31.xml us-gaap-dis-rbtmp03-2020-01-31.xsd us-gaap-dis-sec-suppc-def-2020-01-31.xml
us-gaap-dis-fs-mort-pre-2020-01-31.xml us-gaap-dis-rbtmp03-cal-2020-01-31.xml us-gaap-dis-sec-suppc-pre-2020-01-31.xml
us-gaap-dis-guar-2020-01-31.xsd us-gaap-dis-rbtmp03-def-2020-01-31.xml us-gaap-dis-sec-vq-2020-01-31.xsd
us-gaap-dis-guar-def-2020-01-31.xml us-gaap-dis-rbtmp03-pre-2020-01-31.xml us-gaap-dis-sec-vq-def-2020-01-31.xml
us-gaap-dis-guar-pre-2020-01-31.xml us-gaap-dis-rbtmp04-2020-01-31.xsd us-gaap-dis-sec-vq-pre-2020-01-31.xml
us-gaap-dis-hco-2020-01-31.xsd us-gaap-dis-rbtmp04-cal-2020-01-31.xml us-gaap-dis-sr-2020-01-31.xsd
us-gaap-dis-hco-cal-2020-01-31.xml us-gaap-dis-rbtmp04-def-2020-01-31.xml us-gaap-dis-sr-def-2020-01-31.xml
us-gaap-dis-hco-def-2020-01-31.xml us-gaap-dis-rbtmp04-pre-2020-01-31.xml us-gaap-dis-sr-pre-2020-01-31.xml
us-gaap-dis-hco-pre-2020-01-31.xml us-gaap-dis-rbtmp041-2020-01-31.xsd us-gaap-dis-te-2020-01-31.xsd
us-gaap-dis-iago-2020-01-31.xsd us-gaap-dis-rbtmp041-cal-2020-01-31.xml us-gaap-dis-te-def-2020-01-31.xml
us-gaap-dis-iago-def-2020-01-31.xml us-gaap-dis-rbtmp041-def-2020-01-31.xml us-gaap-dis-te-pre-2020-01-31.xml
us-gaap-dis-iago-pre-2020-01-31.xml us-gaap-dis-rbtmp041-pre-2020-01-31.xml us-gaap-dis-ts-2020-01-31.xsd
us-gaap-dis-iaoi-2020-01-31.xsd us-gaap-dis-rbtmp05-2020-01-31.xsd us-gaap-dis-ts-cal-2020-01-31.xml
us-gaap-dis-iaoi-pre-2020-01-31.xml us-gaap-dis-rbtmp05-cal-2020-01-31.xml us-gaap-dis-ts-def-2020-01-31.xml
us-gaap-dis-ides-2020-01-31.xsd us-gaap-dis-rbtmp05-def-2020-01-31.xml us-gaap-dis-ts-pre-2020-01-31.xml
 
us-gaap-2020-01-31/dqcrules:
dqcrules-0001-def-2020-01-31.xml dqcrules-0008-def-2020-01-31.xml dqcrules-0015-def-2020-01-31.xml dqcrules-2020-01-31.xsd
dqcrules-0001-ref-2020-01-31.xml dqcrules-0008-ref-2020-01-31.xml dqcrules-0015-ref-2020-01-31.xml
 
us-gaap-2020-01-31/elts:
us-arcroles-2020-01-31.xsd us-gaap-depcon-pre-2020-01-31.xml us-gaap-ent-std-2020-01-31.xsd us-gaap-tin-ref-2020-01-31.xml
us-gaap-2020-01-31.xsd us-gaap-doc-2020-01-31.xml us-gaap-lab-2020-01-31.xml us-parts-codification-2020-01-31.xsd
us-gaap-all-2020-01-31.xsd us-gaap-eedm-def-2020-01-31.xml us-gaap-ref-2020-01-31.xml us-parts-tin-2020-01-31.xsd
us-gaap-cn-ref-2020-01-31.xml us-gaap-ent-all-2020-01-31.xsd us-gaap-std-2020-01-31.xsd us-roles-2020-01-31.xsd
us-gaap-depcon-def-2020-01-31.xml us-gaap-ent-all-chg-2020-01-31.xsd us-gaap-tin-def-2020-01-31.xml us-types-2020-01-31.xsd
 
us-gaap-2020-01-31/entire:
us-gaap-entryPoint-all-2020-01-31.xsd us-gaap-entryPoint-std-2020-01-31.xsd
us-gaap-entryPoint-all-wotmp-2020-01-31.xsd us-gaap-entryPoint-tmp-2020-01-31.xsd
 
us-gaap-2020-01-31/META-INF:
catalog.xml taxonomyPackage.xml
 
us-gaap-2020-01-31/stm:
us-gaap-stm-com-2020-01-31.xsd us-gaap-stm-sfp-cls-2020-01-31.xsd us-gaap-stm-soc5-cal-2020-01-31.xml
us-gaap-stm-com-def-2020-01-31.xml us-gaap-stm-sfp-cls-cal-2020-01-31.xml us-gaap-stm-soi-2020-01-31.xsd
us-gaap-stm-com-pre-2020-01-31.xml us-gaap-stm-sfp-cls-def-2020-01-31.xml us-gaap-stm-soi-cal-2020-01-31.xml
us-gaap-stm-scf-dbo-2020-01-31.xsd us-gaap-stm-sfp-cls-pre-2020-01-31.xml us-gaap-stm-soi-def-2020-01-31.xml
us-gaap-stm-scf-dbo-cal-2020-01-31.xml us-gaap-stm-sfp-cls1-cal-2020-01-31.xml us-gaap-stm-soi-egm-2020-01-31.xsd
us-gaap-stm-scf-dbo-def-2020-01-31.xml us-gaap-stm-sfp-cls2-cal-2020-01-31.xml us-gaap-stm-soi-egm-def-2020-01-31.xml
us-gaap-stm-scf-dbo-pre-2020-01-31.xml us-gaap-stm-sfp-dbo-2020-01-31.xsd us-gaap-stm-soi-egm-pre-2020-01-31.xml
us-gaap-stm-scf-dir-2020-01-31.xsd us-gaap-stm-sfp-dbo-cal-2020-01-31.xml us-gaap-stm-soi-indira-2020-01-31.xsd
us-gaap-stm-scf-dir-cal-2020-01-31.xml us-gaap-stm-sfp-dbo-def-2020-01-31.xml us-gaap-stm-soi-indira-pre-2020-01-31.xml
us-gaap-stm-scf-dir-def-2020-01-31.xml us-gaap-stm-sfp-dbo-pre-2020-01-31.xml us-gaap-stm-soi-ins-2020-01-31.xsd
us-gaap-stm-scf-dir-pre-2020-01-31.xml us-gaap-stm-sfp-dbo1-cal-2020-01-31.xml us-gaap-stm-soi-ins-def-2020-01-31.xml
us-gaap-stm-scf-indir-2020-01-31.xsd us-gaap-stm-sfp-ibo-2020-01-31.xsd us-gaap-stm-soi-ins-pre-2020-01-31.xml
us-gaap-stm-scf-indir-cal-2020-01-31.xml us-gaap-stm-sfp-ibo-def-2020-01-31.xml us-gaap-stm-soi-int-2020-01-31.xsd
us-gaap-stm-scf-indir-def-2020-01-31.xml us-gaap-stm-sfp-ibo-pre-2020-01-31.xml us-gaap-stm-soi-int-def-2020-01-31.xml
us-gaap-stm-scf-indir-pre-2020-01-31.xml us-gaap-stm-sfp-sbo-2020-01-31.xsd us-gaap-stm-soi-int-pre-2020-01-31.xml
us-gaap-stm-scf-indira-2020-01-31.xsd us-gaap-stm-sfp-sbo-def-2020-01-31.xml us-gaap-stm-soi-pre-2020-01-31.xml
us-gaap-stm-scf-indira-pre-2020-01-31.xml us-gaap-stm-sfp-sbo-pre-2020-01-31.xml us-gaap-stm-soi-re-2020-01-31.xsd
us-gaap-stm-scf-inv-2020-01-31.xsd us-gaap-stm-sfp-ucreo-2020-01-31.xsd us-gaap-stm-soi-re-def-2020-01-31.xml
us-gaap-stm-scf-inv-cal-2020-01-31.xml us-gaap-stm-sfp-ucreo-def-2020-01-31.xml us-gaap-stm-soi-re-pre-2020-01-31.xml
us-gaap-stm-scf-inv-def-2020-01-31.xml us-gaap-stm-sfp-ucreo-pre-2020-01-31.xml us-gaap-stm-soi-reit-2020-01-31.xsd
us-gaap-stm-scf-inv-pre-2020-01-31.xml us-gaap-stm-sheci-2020-01-31.xsd us-gaap-stm-soi-reit-def-2020-01-31.xml
us-gaap-stm-scf-re-2020-01-31.xsd us-gaap-stm-sheci-cal-2020-01-31.xml us-gaap-stm-soi-reit-pre-2020-01-31.xml
us-gaap-stm-scf-re-def-2020-01-31.xml us-gaap-stm-sheci-def-2020-01-31.xml us-gaap-stm-soi-sbi-2020-01-31.xsd
us-gaap-stm-scf-re-pre-2020-01-31.xml us-gaap-stm-sheci-pre-2020-01-31.xml us-gaap-stm-soi-sbi-def-2020-01-31.xml
us-gaap-stm-scf-sbo-2020-01-31.xsd us-gaap-stm-sheci2-cal-2020-01-31.xml us-gaap-stm-soi-sbi-pre-2020-01-31.xml
us-gaap-stm-scf-sbo-def-2020-01-31.xml us-gaap-stm-soc-2020-01-31.xsd us-gaap-stm-soi1-cal-2020-01-31.xml
us-gaap-stm-scf-sbo-pre-2020-01-31.xml us-gaap-stm-soc-cal-2020-01-31.xml us-gaap-stm-soi4-cal-2020-01-31.xml
us-gaap-stm-scf-sd-2020-01-31.xsd us-gaap-stm-soc-def-2020-01-31.xml us-gaap-stm-spc-2020-01-31.xsd
us-gaap-stm-scf-sd-def-2020-01-31.xml us-gaap-stm-soc-pre-2020-01-31.xml us-gaap-stm-spc-cal-2020-01-31.xml
us-gaap-stm-scf-sd-pre-2020-01-31.xml us-gaap-stm-soc2-cal-2020-01-31.xml us-gaap-stm-spc-def-2020-01-31.xml
us-gaap-stm-sfp-clreo-2020-01-31.xsd us-gaap-stm-soc2-pre-2020-01-31.xml us-gaap-stm-spc-pre-2020-01-31.xml
us-gaap-stm-sfp-clreo-def-2020-01-31.xml us-gaap-stm-soc3-cal-2020-01-31.xml
us-gaap-stm-sfp-clreo-pre-2020-01-31.xml us-gaap-stm-soc4-cal-2020-01-31.xml
```

Yes — exactly. The **XBRL instance document** (the .xml file that companies submit to the SEC) is a **realization** (i.e., an instantiation) of parts of the taxonomy. It does **not** contain the taxonomy itself — instead, it **references** the taxonomy files and then provides actual values, contexts, and facts based on the taxonomy’s structure.

Let me explain clearly how this works in practice, especially for corporate filings (10-K, 10-Q, etc.).

### Key XBRL Components in a Corporate Filing

A typical SEC XBRL submission contains:

| File Type                  | Filename Example (simplified) | What it is / Does |
|----------------------------|-------------------------------|-------------------|
| **Instance document**      | `acme-20241231.xml`           | The main file. Contains: facts (numbers), contexts (periods, entities), units, footnotes. References the taxonomy entry point(s). |
| **Company extension schema** | `acme-20241231.xsd`         | Defines **company-specific** elements (if any) not in US GAAP taxonomy. Usually very small or empty. |
| **Label linkbase**         | `acme-20241231_lab.xml`       | Company-specific labels (optional). |
| **Presentation linkbase**  | `acme-20241231_pre.xml`       | Defines the **order and hierarchy** of elements in the filing (tables, trees). |
| **Calculation linkbase**   | `acme-20241231_cal.xml`       | Defines **summation rules** (e.g., Total Assets = Current Assets + Non-current Assets). |
| **Definition linkbase**    | `acme-20241231_def.xml`       | Defines **dimensional relationships** (e.g., tables with axes like Legal Entity, Class of Stock). |
| **Reference linkbase**     | `acme-20241231_ref.xml`       | Company-specific references (optional). |

### How the Taxonomy Files Are Used

The **instance document** (the .xml file) **references** the US GAAP taxonomy via one or more **entry points**:

```xml
<link:schemaRef xlink:type="simple" xlink:href="http://xbrl.fasb.org/us-gaap/2020/elts/us-gaap-entryPoint-std-2020-01-31.xsd"/>
```

This tells the XBRL processor:  
"Use the US GAAP 2020 taxonomy as the base, starting from this entry point."

From there, the taxonomy pulls in:
- All the **elements** (concepts) from the `elts/` folder schemas.
- All the **presentation trees** from the `stm/` and `dis/` folders (via their `-pre-*.xml` files).
- All the **calculation rules** from the `stm/` and `dis/` folders (via their `-cal-*.xml` files).
- All the **definition relationships** (tables, dimensions) from the `dis/` folder (via `-def-*.xml` files).

The company **does not** need to include those taxonomy files in the submission — they are hosted by the FASB and referenced by URL.

### Specific to Your Question

> "is the presentation linkbase some files in the stm folder?"

Yes, **exactly**:

- The **official presentation trees** for the core financial statements (balance sheet, income statement, cash flow, etc.) are defined in the `stm/` folder's `-pre-*.xml` files.
  - Examples:
    - `us-gaap-stm-sfp-cls-pre-2020-01-31.xml` → Presentation tree for classified balance sheet.
    - `us-gaap-stm-soi-pre-2020-01-31.xml` → Presentation tree for statement of income.
    - `us-gaap-stm-scf-indir-pre-2020-01-31.xml` → Indirect method cash flow statement.

- The **detailed disclosure tables** (footnotes, roll-forwards, etc.) are in the `dis/` folder's `-pre-*.xml` files.
  - Example: `us-gaap-dis-lea-pre-2020-01-31.xml` → Leases disclosure tree.

In the company's filing:
- The **company's presentation linkbase** (`acme-20241231_pre.xml`) **extends** or **references** these taxonomy presentation files.
- Most companies **do not** redefine the entire tree — they **reuse** the taxonomy’s presentation linkbases and just add company-specific extensions or reorderings.

### Summary: What the Instance "Realizes"

| Taxonomy Part                     | Realized in the Filing As |
|-----------------------------------|----------------------------|
| `us-gaap-entryPoint-*.xsd`        | Referenced in the instance document (`<schemaRef>`) |
| Elements (`elts/*.xsd`)           | Used to tag facts in the instance |
| Presentation linkbases (`stm/*-pre*.xml`, `dis/*-pre*.xml`) | Reused / extended in the company’s presentation linkbase |
| Calculation linkbases (`stm/*-cal*.xml`, `dis/*-cal*.xml`) | Reused / extended in the company’s calculation linkbase |
| Definition linkbases (`dis/*-def*.xml`) | Reused / extended in the company’s definition linkbase |

So yes — the **presentation linkbases** you see in the `stm/` and `dis/` folders are the **source** of the official table structures that appear in most corporate filings. The company’s instance document and extension files **build upon** those structures rather than creating them from scratch.

If you have a specific filing (e.g., a 10-K) and want to see how it references or extends these, I can walk you through an example!


Q: in the stm folder, for soi statement of income, for example, why are there so many soi files? are they industry specific? how many different formats of SOI has the XBRL defined?


Yes — the `stm/` folder contains **many** different variations of the **Statement of Income** (SOI) because the US GAAP taxonomy supports **multiple presentation formats** that reflect real-world diversity in how companies present their income statements.

These are **not** primarily industry-specific (though some are more commonly used by certain industries). Instead, they are **format-specific** and **method-specific** variations that the FASB defined to accommodate different acceptable ways companies can present the statement of income under US GAAP.

### Why So Many SOI Files?

The FASB taxonomy includes **all reasonable presentation options** allowed by GAAP, so filers can choose (or slightly adapt) the one that best matches their financial statement format. This avoids forcing every company into one rigid structure.

Here are the main SOI files in the `stm/` folder (from the 2020-01-31 taxonomy you listed) and what they represent:

| File / Pattern                                      | Full Name / Description                                                                 | Common Usage / When Chosen |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------|
| `us-gaap-stm-soi-2020-01-31.xsd`                    | Base schema for SOI (rarely used directly)                                              | —                          |
| `us-gaap-stm-soi-pre-2020-01-31.xml`                | **Standard / Single-step** income statement (most common)                               | General companies, many non-financials |
| `us-gaap-stm-soi-cal-2020-01-31.xml`                | Calculation linkbase for the standard one                                               | —                          |
| `us-gaap-stm-soi-def-2020-01-31.xml`                | Definition linkbase for the standard one                                                | —                          |
| `us-gaap-stm-soi1-cal-2020-01-31.xml`               | Alternative calculation (rare)                                                          | —                          |
| `us-gaap-stm-soi4-cal-2020-01-31.xml`               | Another alternative calculation                                                         | —                          |
| `us-gaap-stm-soi-indira-2020-01-31.xsd`             | **Indirect method** for comprehensive income (rarely used for SOI)                      | —                          |
| `us-gaap-stm-soi-int-2020-01-31.xsd`                | **Insurance-specific** income statement (ASC 944)                                       | Insurance companies        |
| `us-gaap-stm-soi-int-def-2020-01-31.xml`            | Definition for insurance SOI                                                            | Insurance                  |
| `us-gaap-stm-soi-re-2020-01-31.xsd`                 | **Real estate** income statement (ASC 970, REITs)                                       | Real estate investment trusts (REITs) |
| `us-gaap-stm-soi-re-def-2020-01-31.xml`             | Definition for real estate SOI                                                          | REITs                      |
| `us-gaap-stm-soi-reit-2020-01-31.xsd`               | **REIT-specific** income statement                                                      | REITs                      |
| `us-gaap-stm-soi-reit-def-2020-01-31.xml`           | Definition for REIT SOI                                                                 | REITs                      |
| `us-gaap-stm-soi-sbi-2020-01-31.xsd`                | **Single-step** income statement (alternative presentation)                             | General (less common)      |
| `us-gaap-stm-soi-egm-2020-01-31.xsd`                | **Earnings before extraordinary items** (rare, legacy)                                  | Older filings              |

### How Many Different Formats Does the Taxonomy Define?

In the 2020-01-31 taxonomy, there are **about 7–8 distinct presentation formats** for the Statement of Income (SOI), depending on how you count variations:

| Format / Variation                          | Count | Primary User Group                  | Key Characteristics |
|---------------------------------------------|-------|-------------------------------------|---------------------|
| 1. **Standard single-step** (most common)   | 1     | Most non-financial companies        | Revenue → Expenses → Net Income |
| 2. **Multi-step** (gross profit, operating income) | 1     | Retail, manufacturing               | Includes gross profit subtotal |
| 3. **Insurance-specific** (ASC 944)         | 1     | Insurance companies                 | Premiums, benefits, expenses |
| 4. **Real estate / REIT-specific**          | 2     | REITs, real estate                  | Rental income, property expenses |
| 5. **Single-step alternative**              | 1     | General (less common)               | Simpler structure |
| 6. **Earnings before extraordinary items**  | 1     | Legacy / rare                       | Pre-2015 GAAP feature |
| 7. **Other minor variations**               | 1–2   | Specific cases                      | Calculation or definition tweaks |

**Total distinct SOI formats**: **~7 main ones**, with the **standard single-step** being by far the most commonly used.

### Why Not Just One Format?

US GAAP allows flexibility in presentation:
- Some companies present a **multi-step** income statement (gross profit → operating income → net income).
- Others use **single-step** (all revenues minus all expenses).
- Insurance and REITs have **industry-specific** line items and subtotals required by ASC 944 and ASC 970/974.

The taxonomy provides **separate presentation trees** for each so companies can pick the one closest to their actual financial statements and minimize extensions.

### Practical Impact in Filings

- Most non-financial companies use the **standard single-step** tree (`us-gaap-stm-soi-pre-2020-01-31.xml`).
- Insurance companies almost always use the insurance-specific one.
- REITs use the real estate or REIT-specific versions.
- Companies rarely create completely custom SOI trees — they usually extend or slightly reorder one of these taxonomy-provided trees.

So yes — the large number of SOI files exists to cover **legitimate presentation differences** under GAAP, not just industry specificity (though industry does play a role for insurance and REITs).

Let me know if you want me to pull up the exact line items or structure for one of these (e.g., standard vs. insurance vs. REIT)!


Q: can I find a company's SOI type in its instance file or in which of the linkbase file?

Yes — you can determine which **Statement of Income (SOI) type/format** a company is using by looking in **specific places** in their XBRL submission files. Here’s exactly where and how to find it.

### Quick Answer: Where to Look

| Location in the Filing                              | How to Identify the SOI Type | Details |
|-----------------------------------------------------|------------------------------|---------|
| **Presentation linkbase** (usually `company-YYYYMMDD_pre.xml`) | **Best and most direct** way | Look for `<link:loc>` and `<link:presentationArc>` elements that reference US GAAP presentation linkbases in `stm/`. The referenced file name reveals the SOI type. |
| **Instance document** (the main `.xml` file)        | Indirectly (via schema references) | See which entry point or schema is referenced — but this is less precise. |
| **Definition linkbase** (`company-YYYYMMDD_def.xml`) | Sometimes helpful | If the company uses a dimensional table for SOI, it may reference a specific `stm-soi-*-def-*.xml`. |

### Most Reliable Way: Check the **Presentation Linkbase**

The company’s **presentation linkbase** (`*_pre.xml`) explicitly tells you which US GAAP SOI format they are using.

#### Step-by-Step: How to Find It

1. Open the company’s **presentation linkbase** file (e.g., `acme-20241231_pre.xml`).
2. Search for **references to US GAAP presentation trees** in the `<link:loc>` elements.
3. Look for a `<link:loc>` that points to one of these US GAAP files in the `stm/` folder:

| US GAAP File Referenced (in `<link:loc xlink:href="...">`) | SOI Type / Format Used |
|------------------------------------------------------------|------------------------|
| `http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-pre-2020-01-31.xml` | **Standard single-step** (most common) |
| `http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-sbi-pre-2020-01-31.xml` | **Single-step alternative** |
| `http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-int-pre-2020-01-31.xml` | **Insurance-specific** (ASC 944) |
| `http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-re-pre-2020-01-31.xml` | **Real estate-specific** |
| `http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-reit-pre-2020-01-31.xml` | **REIT-specific** |
| `http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-egm-pre-2020-01-31.xml` | **Earnings before extraordinary items** (legacy/rare) |

- The **xlink:href** value will point to one of the above.
- If you see a reference to `us-gaap-stm-soi-pre-2020-01-31.xml`, the company is using the **standard single-step SOI** (by far the most common).

#### Example Snippet from a Real Filing’s Presentation Linkbase

```xml
<link:loc xlink:type="locator" xlink:href="http://xbrl.fasb.org/us-gaap/2020/stm/us-gaap-stm-soi-pre-2020-01-31.xml#us-gaap_IncomeStatementAbstract" xlink:label="loc_us-gaap_IncomeStatementAbstract"/>
```

This means: **"This company is using the standard single-step SOI tree from the US GAAP taxonomy."**

### Other Clues (Less Direct)

- **Instance document**: Look at the `<link:schemaRef>` — if it references `us-gaap-entryPoint-all-2020-01-31.xsd` or `us-gaap-entryPoint-std-2020-01-31.xsd`, it includes all SOI formats, but doesn’t tell you **which one** the company chose. You still need the presentation linkbase.
- **Definition linkbase**: Sometimes a company will reference a specific `stm-soi-*-def-*.xml`, which can also indicate the format.

### Practical Tools to Check Quickly

- **Arelle Viewer** (free): Load the instance document → View → Presentation → Look for the "Income Statement" tree → Right-click → "View Source" to see which taxonomy file it’s pulling from.
- **SEC EDGAR Viewer**: Go to a filing → "Interactive Data" → "View Excel Document" or "View Instance" → Look at the income statement table and see if it matches standard, insurance, REIT, etc.
- **Text search**: In the `_pre.xml` file, search for `stm-soi` — you’ll quickly see which one is referenced.

### Summary

- **Primary place**: The **presentation linkbase** (`*_pre.xml`) — look for a `<link:loc>` referencing a `us-gaap-stm-soi-*-pre-*.xml` file.
- Most companies use the **standard single-step** (`us-gaap-stm-soi-pre-2020-01-31.xml`).
- Insurance companies use `us-gaap-stm-soi-int-pre-...`.
- REITs use `us-gaap-stm-soi-re-...` or `us-gaap-stm-soi-reit-...`.

If you have a specific company’s filing (e.g., ticker or CIK), I can help you look up which SOI type they used!

