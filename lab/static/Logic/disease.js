
var myApp = angular.module("myApp", []);
myApp.config(function($interpolateProvider){
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});
myApp.factory("dictionary", function () {
  var dis_object = {};
  dis_object.number = category;

  return dis_object;
});

myApp.controller("thisapp", function ($scope, dictionary) {
  
  $scope.dis_category = dictionary.number;
  console.log($scope.dis_category)
  $scope.specific = {};
  console.log("Hello",$scope.specific);
  $scope.assign = function(que){
    console.log("Inside functiion");
    $scope.specific = que ;
    console.log($scope.specific);
  };
});

var category = [
  {
    Advice:
      "Not all haemopoietic cells or ‘blood cells’ are erythrocytes (red blood cells). This term is often used to encompass lymphocytes, macrophages, granulocytes and other white cell types. Check the context of the research.e.g. if the research relates to leukaemia it will be referring to lymphocytes etc. and not to erythrocytes and therefore should be coded as Cancer and not be coded as Blood.Studies investigating blood flow to the brain should be coded as Stroke.Blood clots (thromboses) can lead to wider cardiovascular complications and stroke. In these circumstances code to the primary condition of focus ignoring pathogenesis, but following rules for sequelae where appropriate.",
    type: "Blood",
    desc:
      "Haematological diseases, anaemia, clotting (including thromboses and venous embolisms) and normal development and function of platelets and erythrocytes",
  },
  {
    Advice:
      "Do not code to the site of the cancer. However if the research involves studying a condition that predisposes to cancer then it may be appropriate to code for this condition as well. e.g. The role of Barrett’s oesophagus in cancer would be 50% Oral and Gastrointestinal and 50% Cancer. Similarly research on pathogens associated with the development of cancer should be coded as 50% Cancer and 50% Infection. Studies of the normal role of oncogenes, tumour suppressor genes, and cell cycle checkpoints in a non diseased cell should be coded as 50% Generic Health Relevance and 50% Cancer. Excludes general studies of angiogenesis which should be coded as Cardiovascular. However the development of anti-angiogenic drugs to inhibit tumour growth would be coded as Cancer. Excludes normal studies of cell cycle and DNA replication and repair which should be coded as Generic.",
    type: "Cancers and Neoplasms",
    desc:
      "All types of neopIncludes general circulation research, vasculitis and general angiogenesis studies. Includes atherosclerosis and pulmonary hypertension. Includes congenital heart disorders. Excludes studies investigating blood flow to the brain which should be coded as Stroke. Excludes angiogenesis studies which relate to a diseased state .",
  },
  {
    Advice:
      "Includes general circulation research, vasculitis and general angiogenesis studies. Includes atherosclerosis and pulmonary hypertension. Includes congenital heart disorders. Excludes studies investigating blood flow to the brain which should be coded as Stroke. Excludes angiogenesis studies which relate to a diseased state (e.g. development of anti-angiogenic drugs to inhibit tumour growth which would be coded as Cancer).",
    type: "CardioVascular",
    desc:
      "Coronary heart disease, diseases of the vasculature and circulation including the lymphatic system, and normal development and function of the cardiovascular system",
  },
  {
    Advice:
      "Includes physical malformation and congenital syndromes that are associated with multiple diseases and conditions. Excludes inherited single disease disorders (even when referred to as ‘congenital’) which should be coded under the appropriate Health Category.",
    type: "Congential Disorders",
    desc:
      "Physical abnormalities and syndromes that are not associated with a single type of disease or condition including Down’s syndrome and cystic fibrosis",
  },
  {
    Advice:
      "Includes normal studies on this organ or the condition of deafness. Studies that involve the auditory nerve leading to the brain may be double coded as 50% Neurological and 50% Ear as appropriate. Excludes mapping of hearing in regions of the brain in which case the Neurological category should be applied.",
    type: "Ear",
    desc: "Deafness and normal ear development and function",
  },
  {
    Advice:
      "Includes normal studies on this organ or the condition of blindness. Studies that involve the optic nerve leading to the brain may be double coded as 50% Neurological and 50% Eye as appropriate. Excludes mapping of vision in regions of the brain in which case the Neurological category should be applied.",
    type: "Eye",
    desc: "Diseases of the eye and normal eye development and function",
  },
  {
    Advice:
      "Infection should be used for all research on pathogens and diseases caused by infection. These studies should be coded as 100% Infection and should not also be coded to the target disease site.Studies involving acute immune response to infection should be coded as Infection. However studies of natural tolerance and immunity to infections should be coded as 100% Inflammatory and Immune System.",
    type: "Infection",
    desc:
      "Diseases caused by pathogens, acquired immune deficiency syndrome, sexually transmitted infections and studies of infection and infectious agents",
  },
  {
    Advice:
      "Includes listed immune diseases and studies of normal immune response. Also includes natural tolerance and immunity to infections. However studies involving the acute immune response to infection should be coded as Infection; in general, any research with a specified infectious / pathogenic agent should only be coded as Infection.",
    type: "Inflammatory and Immune system",
    desc:
      "Rheumatoid arthritis, connective tissue diseases, autoimmune diseases, allergies and normal development and function of the immune system",
  },
  {
    Advice:
      "This category is designed to capture research directly relating to external accidents, injuries and physical trauma and should not include endogenous studies of damage such as ischemic injury. Intervention studies preventing or treating falls should be coded to Injuries and Accidents. It may be appropriate to also code for specific conditions if the study involves a particular patient group. Excludes studies of wound healing, unless the wound was acquired by accident.",
    type: "Injuries and Accidents",
    desc: "Fractures, poisoning and burns",
  },
  {
    Advice:
      "Mental Health should be used for all normal cognitive research categorised to 1.2 Psychological i.e. behaviour learning, memory, language, perception etc. Studies dealing with the brain of individuals with a psychological condition listed in the Mental Health category should be coded as 100% Mental Health and not as Neurological.",
    type: "Mental health",
    desc:
      "Depression, schizophrenia, psychosis and personality disorders, addiction, suicide, anxiety, eating disorders, learning disabilities, bipolar disorder, autistic spectrum disorders and studies of normal psychology, cognitive function and behaviour.",
  },
  {
    Advice:
      "This category includes basic studies of metabolism but not generic signalling pathways involving kinases. This includes studies of metabolic regulation – the means by which nutrients are converted into energy – and the conditions which affect the ability of these processes to be carried out. For example regulation of blood lipids and cholesterol are classified as Metabolic and Endocrine. Studies on nutrition, diet and obesity and/or physical activity and exercise are context based and should only be coded as Metabolic if they relate to metabolism.",
    type: "Metabolic and endocrine",
    desc:
      "Metabolic disorders (including Diabetes) and normal metabolism and endocrine development and function. This includes all research on the pineal, thyroid, parathyroid, pituitary and adrenal glands.",
  },
  {
    Advice:
      "Includes research into limbs and the face. Studies of musculoskeletal pain, such as fibromyalgia, should be classified as Musculoskeletal. However studies focussed on pain pathways in the nervous system would be classified as Neurological and pain perception would be classified as Mental Health.",
    type: "Musculoskeletal",
    desc:
      "Osteoporosis, osteoarthritis, muscular and skeletal disorders and normal musculoskeletal and cartilage development and function.",
  },
  {
    Advice:
      "This category is suitable for studies of the ‘wiring’ of the brain. Includes studies of TSEs, CJD and prion protein. Studies on circadian rhythm are often but not always Neurological. Other conditions where disruption to circadian rhythm is linked to disease should be coded to the appropriate health category. For example, circadian influence on immune cells in rheumatoid arthritis would be coded as Inflammatory and Immune System. Studies on headaches and migraine are often but not always Neurological. Headaches resulting from other conditions may require alternative or additional health categories, following the rules for sequelae. For example, headaches resulting from visual impairments can be coded 50% Eye, 50% Neurological.",
    type: "Neurological",
    desc:
      "Dementias, transmissible spongiform encephalopathies, Parkinson’s disease, neurodegenerative diseases, Alzheimer’s disease, epilepsy, multiple sclerosis and studies of the normal brain and nervous system.",
  },
  {
    Advice:
      "Inflammatory bowel disease, Crohn’s disease, diseases of the mouth, teeth, oesophagus, digestive system including liver and colon, and normal oral and gastrointestinal development and function.",
    type: "Oral and gastrointestinal",
    desc:
      "Includes dental research and studies on the mouth, throat, stomach, liver, pancreas (not diabetes/insulin related), gut and colon. Also suitable for problems linked to food absorption by the gut.",
  },
  {
    Advice:
      "Includes female and male sexual organs and associated diseases where the research is not directly linked to reproductive issues such as developmental studies.",
    type: "Renal and urogenital",
    desc:
      "Kidney disease, pelvic inflammatory disease, renal and genital disorders, and normal development and function of male and female renal and urogenital system.",
  },
  {
    Advice:
      "Includes studies of ante and post natal care such as issues affecting newborns. Includes studies of the effects of exposure to factors while in utero if focussed on the foetus or newborns. If the study is about the long term effects on children or adults, where the foetus is not involved in the investigation, the Reproductive Health and Childbirthcategory should not be used.",
    type: "Reproductive health and childbirth",
    desc:
      "Fertility, contraception, abortion, in vitro fertilisation, pregnancy, mammary gland development, menstruation and menopause, breast feeding, antenatal care, childbirth, postnatal care and complications of newborns.",
  },
  {
    Advice:
      "Includes studies of the upper and lower respiratory tract, including nasal cavity, sinuses, larynx, vocal cords, trachea and lungs. Studies of the elements of the throat shared with the digestive system (e.g. pharynx and epiglottis) may be coded as Oral and Gastrointestinal depending on the context of the research.",
    type: "Respiratory",
    desc:
      "Asthma, chronic obstructive pulmonary disease (COPD), respiratory diseases and normal development and function of the respiratory system.",
  },
  {
    Advice:
      "Many dermatological conditions are associated with an inflammatory or allergic response. Code to the disease under investigation and not to the accompanying response. This means conditions such as psoriasis and eczema would normally be coded as 100% Skin. However studies of allergies in patients with dermatological conditions can be coded as 50% Inflammatory and Immune System for allergies and 50% Skin.",
    type: "Skin",
    desc: "Dermatological conditions and normal skin development and function.",
  },
  {
    Advice:
      "When coding research involving circulation or blood flow, only studies investigating blood flow to the brain should be coded as Stroke. While general blood circulation and cardiovascular disease research should be coded as Cardiovascular, research involving blood flow to brain should be coded as Stroke. Therefore haemorrhagic stroke will generally be coded as 100% Stroke unless there is a clear pre-existing condition, in which case the guidance on sequelae should be followed",
    type: "Stroke",
    desc:
      "Well had to work again",
  },
];
