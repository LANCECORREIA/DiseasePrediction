import keras.utils as image
import numpy as np
from keras.models import load_model
import os
from django.conf import settings

model = load_model(os.path.join(settings.BASE_DIR,"model/model.h5"))

disease_class = [
    "Pepper__bell___Bacterial_spot",
    "Pepper__bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato_Bacterial_spot",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_Leaf_Mold",
    "Tomato_Septoria_leaf_spot",
    "Tomato_Spider_mites_Two_spotted_spider_mite",
    "Tomato__Target_Spot",
    "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato__Tomato_mosaic_virus",
    "Tomato_healthy",
]

disease_info = [
 {
  "Crop": "Pepper__bell",
  "Disease": "Bacterial_spot",
  "Cause": " Bacterial spot occurs worldwide and is one of the most devastating diseases on pepper crops grown in warm, moist environments.  The pathogen can survive in association with seeds, either externally or internally as well as on specific weeds and later spreads through rain or overhead irrigation. It enters the plant through leaf pores and wounds. ",
  "Treatment": " Bacterial spot occurs worldwide and is one of the most devastating diseases on pepper and tomato crops grown in warm, moist environments.  The pathogen can survive in association with seeds, either externally or internally as well as on specific weeds and later spreads through rain or overhead irrigation. It enters the plant through leaf pores and wounds. "
 },
 {
  "Crop": "Pepper__bell",
  "Disease": "Healthy",
  "Cause": "NA",
  "Treatment": "NA"
 },
 {
  "Crop": "Potato",
  "Disease": "Early_blight",
  "Cause": "Early blight of potato is a disease caused by fungal species.Prolonged period of wetness on the plants.Circular dark brown rings or lesions on older leaves, that spread to stems and leaves gradually.",
  "Treatment": " Varieties resistant to this disease are available. In general, late maturing varieties are more resistant than the earlier maturing varieties. Keep plants healthy; stressed plants are more predisposed to early blight. Avoid overhead irrigation. Do not dig tubers until they are fully mature in order to prevent damage."
 },
 {
  "Crop": "Potato",
  "Disease": "Late_blight",
  "Cause": "Late blight of potato is a disease caused by oomycetes, which is a distant relative of fungi.The spores tend to spread in cool and wet conditions.Irregular-shaped lesions on the leaves, petioles and stems, the potato tubers start to rot, a whitish cottony growth of fungus is visible on the whole plant",
  "Treatment": "Use disease-free seed potatoes. Keep cull\/compost piles away from potato growing areas. Destroy any volunteer potato plants. Keep tubers covered with soil throughout the season to prevent tuber infection. Remove infected tubers before storing to prevent the spread of disease in storage. Kill vines completely before harvest to avoid inoculation of the tubers during harvest. "
 },
 {
  "Crop": "Potato",
  "Disease": "Healthy",
  "Cause": "NA",
  "Treatment": "NA"
 },
 {
  "Crop": "Tomato",
  "Disease": "Bacterial_spot",
  "Cause": "These bacterial pathogens can be introduced into a garden on contaminated seed and transplants, which may or may not show symptoms.  The pathogens enter plants through natural openings (e.g., stomates), as well as through wounds. ",
  "Treatment": "A plant with bacterial spot cannot be cured.  Remove symptomatic plants from the field or greenhouse to prevent the spread of bacteria to healthy plants."
 },
 {
  "Crop": "Tomato",
  "Disease": "Early_blight",
  "Cause": " Early blight symptoms usually begin after the first fruits appear on tomato plants, starting with a few small, brown lesions on the bottom leaves. As the lesions grow, they take the shape of target-like rings, with dry, dead plant tissue in the center. The surrounding plant tissue turns yellow, then brown before the leaves die and fall off the plant.2 While early blight does not directly affect fruits, the loss of protective foliage can cause damage to fruits due to direct sun exposure. That condition is known as sun scald.",
  "Treatment": "Once blight is positively identified, act quickly to prevent it from spreading. Remove all affected leaves and burn them or place them in the garbage. Mulch around the base of the plant with straw, wood chips or other natural mulch to prevent fungal spores in the soil from splashing on the plant."
 },
 {
  "Crop": "Tomato",
  "Disease": "Late_blight",
  "Cause": "Late blight can affect tomato plants at any point in the growing season and at any stage of growth. Symptoms appears at the edge of tomato leaves, with dark, damaged plant tissue that spreads through the leaves toward the stem. White mildew may grow on the lower leaf surface of the affected area. This type of blight progresses rapidly through plants in humid conditions,3 and if left untreated, can spread to fruits.",
  "Treatment": "Once blight is positively identified, act quickly to prevent it from spreading. Remove all affected leaves and burn them or place them in the garbage. Mulch around the base of the plant with straw, wood chips or other natural mulch to prevent fungal spores in the soil from splashing on the plant."
 },
 {
  "Crop": "Tomato",
  "Disease": "Leaf_Mold",
  "Cause": "Tomato leaf mold is caused by a fungal pathogen called Passalora fulva (syn. Cladosporium fulvum). It is an ascomycete fungus that lives on living tomato leaves. The fungus produces conidia that infect the lower surfaces of leaves.",
  "Treatment": " Seed treatment with hot water (25 minutes at 122 °F or 50 °C) is recommended to avoid the pathogen on seeds.  "
 },
 {
  "Crop": "Tomato",
  "Disease": "Septoria_leaf_spot",
  "Cause": "Septoria leaf spot is caused by the fungus Septoria lycopersici. This fungus can attack tomatoes at any stage of development, but symptoms usually first appear on the older, lower leaves and stems when plants are setting fruit.",
  "Treatment": "The effects of Septoria leaf spot can be minimized by following a multifaceted approach to disease management that includes sanitary, cultural, and chemical methods. It is very important to eliminate initial sources of inoculum by removing or destroying as much of the tomato debris as possible after harvest in the fall."
 },
 {
  "Crop": "Tomato",
  "Disease": "Spider_mites_Two_spotted_spider_mite",
  "Cause": "Tomato red spider mite feeding causes whitening or yellowing of leaves, which then dry out and eventually fall off. In the case of severe attacks, plant damage progresses very quickly, and hosts may die within 3–5 weeks, if no management actions are taken.",
  "Treatment": "Spider mite populations are held down in cool conditions early in the season by various predators such as pirate and big-eyed bugs. Predator mites are effective predators of spider mites and are available."
 },
 {
  "Crop": "Tomato",
  "Disease": "Target_spot",
  "Cause": "Target spot of tomato caused by Corynespora cassiicola, is a serious foliar disease of both greenhouse and field grown tomatoes. The field disease is limited to the tropical and subtropical regions of the world.",
  "Treatment": "Remove old plant debris at the end of the growing season; otherwise, the spores will travel from debris to newly planted tomatoes in the following growing season, thus beginning the disease anew. Dispose of the debris properly and don’t place it on your compost pile unless you’re sure your compost gets hot enough to kill the spores."
 },
 {
  "Crop": "Tomato",
  "Disease": "Tomato_YellowLeaf_Curl_Virus",
  "Cause": "Nutrient Deficiency is a Likely Cause. The most common reason why the leaves on established tomato plants turn yellow is a lack of nutrients in the soil. Tomatoes are extremely heavy feeders and require plenty of nutrients to grow healthy and be fruitful",
  "Treatment": "Management of TYLCV includes reducing viral inoculum by destroying crop residues, using reflective mulches to repel the vector in early stages of crop growth, planting TYLCV-resistant varieties when appropriate, and treating plants with a combination of at-plant, drip injected, and foliar insecticides"
 },
 {
  "Crop": "Tomato",
  "Disease": "Tomat_mosaic_virus",
  "Cause": "The tomato potyviruses are transmitted plant-to-plant by many species of aphids. Aphids only retain the ability to transmit these viruses for very short periods of time (minutes to a few hours). Thus, spread is often very rapid and localized.",
  "Treatment": "Once plants are infected, there is no cure for mosaic viruses. Because of this, prevention is key! However, if plants in your garden do show symptoms of having mosaic viruses, here’s how to minimize the damage: Remove all infected plants and destroy them. Do NOT put them in the compost pile, as the virus may persist in infected plant matter. Burn infected plants or throw them out with the garbage."
 },
 {
  "Crop": "Tomato",
  "Disease": "Healthy",
  "Cause": "NA",
  "Treatment": "NA"
 }
]

def predict(img):
    
    img = image.img_to_array(img)
    img = np.expand_dims(img,axis=0)
    img /= 255
    return disease_info[np.argmax(model.predict(img)[0])] 

if __name__  == "__main__":
    img = image.load_img('tom_sep.jpg', grayscale=False, target_size=(64, 64))
    show_img=image.load_img('tom_sep.jpg', grayscale=False, target_size=(200, 200))
    print("Prediction:",predict(img))
