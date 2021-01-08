var myApp = angular.module("selfAssess", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("assessControl", function ($scope) {
  $scope.question = [
    {
      question: "Are you experiencing any of the symptoms listed below?",
      possible: [
        {
          ans: "Fever",
        },
        {
          ans: "Cough",
        },
        {
          ans: "Shortness of breath",
        },
        {
          ans: "Loss of appetite or sense of smell",
        },
        {
          ans: "None of these",
        },
      ],
    },
    {
      question:
        "Within 14 days of the start of your symptoms, did you travel to an area of high-risk for COVID-19 either in the US or abroad or have you been in close contact with someone who traveled to one of those areas?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "Within 14 days of the start of your symptoms, have you had contact with a person confirmed to have COVID-19?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
        {
          ans: "Dont Know",
        },
      ],
    },
    {
      question:
        "Do you have high blood pressure, diabetes, heart disease, lung disease, or kidney disease?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "COVID-19 can affect people who have weaker immune systems from things like chemotherapy, HIV/AIDS, organ transplant, or prolonged steroid use. Do you have a weakened immune system?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question: "Are you over the age of 65?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question: "Are you over the age of 65?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "Based on your responses, it seems like you aren't showing any symptoms but you may have been exposed to the virus. Stay at home and monitor for symptoms, such as fever, cough, or shortness of breath. Should you develop symptoms, call your primary care doctor for additional advice.",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "Do you have severe shortness of breath, crushing chest pain, bluish lips or face, or any other life-threatening symptoms?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "Do you have severe shortness of breath, crushing chest pain, bluish lips or face, or any other life-threatening symptoms?",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "Based on your responses, it seems like your situation is urgent. You should go to the nearest Emergency Room. If you cannot safely get there on your own, call 911. IMPORTANT: You should call ahead to make sure the ER can prepare for your arrival. Be sure to tell them that you were potentially exposed to the coronavirus and you also have severe difficulty breathing.",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
    {
      question:
        "Based on your responses, it seems like you are not feeling your best and you may benefit from talking with your primary care doctor to discuss your symptoms and assess your risks for COVID-19.",
      possible: [
        {
          ans: "Yes",
        },
        {
          ans: "No",
        },
      ],
    },
  ];
});
