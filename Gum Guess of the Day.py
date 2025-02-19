import random
try:
    import clipboard  # Try to import Pythonista's clipboard module
except ImportError:
    try:
        import pyperclip  # Try to import pyperclip for desktop
    except ImportError:
        print("Note: Neither clipboard nor pyperclip module found. Copy functionality will be disabled.")
        print("To enable copying, install pyperclip using: pip install pyperclip")

# Embedded question bank
QUESTIONS = [
    {
        "question": "The protocol for dental trauma involves all of the following, except",
        "options": [
            "Ideally, the tooth should be repositioned to its original position.",
            "EPT and thermal testing are unreliable following trauma since physical trauma can severe or damage nerve supply without altering pulpal blood supply/vitality.",
            "If the root is completely formed on a tooth that has been intruded, a pulpectomy should be performed within 1-3 weeks after the injury.",
            "The tooth should be splinted for 2 to 4 months if it sustains a root fracture"
        ],
        "correct_answer": "The tooth should be splinted for 2 to 4 months if it sustains a root fracture"
    },
    {
        "question": "When evaluating horizontal root fractures, one should consider all as being true, except:",
        "options": [
            "Chances of coronal root fractures healing are similar to mid-root or apical fractures if the fracture is below the height of crestal bone and properly splinted",
            "If the fracture is at or coronal to the crest of the alveolar bone, the prognosis is still favorable",
            "Pulpal necrosis occurs in 25% of root fractures",
            "In the vast majority of cases, necrosis occurs in the coronal segment only with the apical segment remaining vital"
        ],
        "correct_answer": "If the fracture is at or coronal to the crest of the alveolar bone, the prognosis is still favorable"
    },
    {
        "question": "How long should horizontal root fractures be splinted if the coronal section was displaced and repositioned?",
        "options": [
            "Not indicated",
            "7 to 10 days",
            "4 to 6 weeks",
            "3 months"
        ],
        "correct_answer": "4 to 6 weeks"
    },
    {
        "question": "Which of the following techniques is the best way to detect a vertical root fractures?",
        "options": [
            "Periapical Film",
            "Panograph",
            "CAT Scan",
            "Occlusal Film"
        ],
        "correct_answer": "CAT Scan"
    },
    {
        "question": "Patient presents for emergency dental exam after falling off his bike and face planted into sidewalk. Upon examination, you suspect that he may have a root fracture of #8. How many angled PA radiographs would you take, at a minimum?",
        "options": [
            "Two angled films at 45 and 90 degrees to the possible fracture line",
            "Only one film from the distal or mesial at 45 degree to uphold ALARA,",
            "Three angled films at 45, 90 and 110 degrees to ensure at least one passes through the possible fracture line",
            "Two angle films at any angle as long as it is parallel to the long axis of the root and will reveal the fracture line."
        ],
        "correct_answer": "Three angled films at 45, 90 and 110 degrees to ensure at least one passes through the possible fracture line"
    },
    {
        "question": "Assessment of a completed NSRCT is based primarily on what?",
        "options": [
            "Radiographic examination",
            "Pain level of the patient",
            "Mobility of the tooth",
            "EPT results",
            "The alignment of the planets"
        ],
        "correct_answer": "Radiographic examination"
    },
    {
        "question": "Research has demonstrated that the average distance from the foramen to the minor constriction is:",
        "options": [
            "0.5 -1.0mm",
            "0.2-0.4mm",
            "1.0-2.0mm",
            "2.0-3.0mm"
        ],
        "correct_answer": "0.5 -1.0mm"
    },
    {
        "question": "Which of the following diagnostic tests is (are) not an indication of pulp vitality? 1. Percussion 2. Mobility 3. Thermal (hot and cold)",
        "options": [
            "1 only",
            "3 only",
            "1 and 2",
            "2 and 3",
            "All of the above"
        ],
        "correct_answer": "1 and 2"
    },
    {
        "question": "Which of following is false with respect to the use of electric pulp testing in endodontics?",
        "options": [
            "The technology is not accurate enough at this time to be utilized on a routine basis in a clinical setting.",
            "The response of the pulp to electric testing reflects the histologic health or disease status of the pulp.",
            "A response by the pulp to the electric current only denotes that some viable nerve fibers are present in the pulp and are capable of responding.",
            "Electric pulp test results are most accurate when no response is obtained to any amount of current (i.e. necrotic pulp)."
        ],
        "correct_answer": "The response of the pulp to electric testing reflects the histologic health or disease status of the pulp."
    },
    {
        "question": "To date, the most accurate pulp test that are used to determine if a tooth's pulp is healthy is/are",
        "options": [
            "Cold",
            "Heat",
            "EPT",
            "Both a and b",
            "Both a and c"
        ],
        "correct_answer": "Both a and c"
    },
    {
        "question": "When applying the tube shift technique, buccal object rule, Clark's rule, or the SLOB rule - all being the same concept - one should realize all of the following except:",
        "options": [
            "Can be used to locate additional canals or roots and distinguish between objects that have been superimposed",
            "Distinguishes between various types of resorption and helps locate foreign bodies",
            "The object closest to the buccal surface appears to move in the direction opposite the movement of the tube head",
            "The object farthest from the film moves farthest on the film with respect to a change in horizontal angulation of the radiograph tube head",
            "All are true"
        ],
        "correct_answer": "All are true"
    },
    {
        "question": "An advantage of the Gow-Gates mandibular block over the Akinosi technique includes all the following except:",
        "options": [
            "Higher success rate 97.25%",
            "Presence of bony contact to provide a landmark prior to injection of solution",
            "A high positive aspiration rate",
            "Highly successful in patients with limited opening"
        ],
        "correct_answer": "Highly successful in patients with limited opening"
    },
    {
        "question": "Which of the following is not a landmark for the Akinosi block?",
        "options": [
            "Maxillary Tuberosity",
            "Pterygomandibular Raphe",
            "Coronoid Notch",
            "Mucogingival Junction of the maxillary third"
        ],
        "correct_answer": "Pterygomandibular Raphe"
    },
    {
        "question": "Your first two attempts with conventional IAN block to anesthesize a patient with irreversible pulpitis was ineffective during the pulpectomy procedure, which adjunctive technique will more likely increase your success rate on the second attempt?",
        "options": [
            "Gow Gates technique",
            "Buccal and lingual infiltration",
            "Vazirani-Akinosi technique",
            "None of the above"
        ],
        "correct_answer": "Gow Gates technique"
    },
    {
        "question": "What type of nonavulsive tooth displacement has the worst prognosis?",
        "options": [
            "Extrusion",
            "Intrusion",
            "Subluxation",
            "Lateral luxation"
        ],
        "correct_answer": "Intrusion"
    },
    {
        "question": "Subluxation refers to ________ and is treated ____________.",
        "options": [
            "Displacement labially, lineally, distally, or incisally; repositioning the tooth into normal position, take x-ray after repositioning, stabilize with flexible splint for up to 3 weeks",
            "No displacement normal mobility, and sensitivity to percussion; flexible splint is optional, may be used for pt comfort for 7-10 days",
            "Sensitivity to percussion, increased mobility, no displacement; flexible splint is optional, may be used for the comfort of the patient for 7-10 days",
            "Displacement in a coronal direction; reposition, stabilize the tooth with a flexible splint for up to 3 weeks"
        ],
        "correct_answer": "Sensitivity to percussion, increased mobility, no displacement; flexible splint is optional, may be used for the comfort of the patient for 7-10 days"
    },
    {
        "question": "Which of the following scenarios and clinical management would be considered the incorrect preparation of a root during avulsion of a permanent tooth?",
        "options": [
            "Extraoral dry time less than 60 minutes with closed apex: The root should be rinsed of debris with water or saline, replant and apply flexible splint for 1-2 weeks, initiate endodontic treatment with calcium hydroxide at 7-10 days.",
            "Extraoral dry time less than 60 minutes with open apex: The root should be rinsed of debris with water or saline, soak in doxycycline for 5 minutes, replant, initiate endodontic treatment with calcium hydroxide at 7-10 days (apexification) or allow for revascularization.",
            "Extraoral dry time more than 60 minutes with closed apex: Remove debris and necrotic periodontal ligament, soak in 2% stannous fluoride, replant, initiate endodontic treatment with calcium hydroxide at 7-10 days (apexification) or allow for revascularization.",
            "Extraoral dry time more than 60 minutes with open apex: Replantation usually is not indicated"
        ],
        "correct_answer": "Extraoral dry time more than 60 minutes with closed apex: Remove debris and necrotic periodontal ligament, soak in 2% stannous fluoride, replant, initiate endodontic treatment with calcium hydroxide at 7-10 days (apexification) or allow for revascularization."
    },
    {
        "question": "EDTA or ethylenediamine tetra acetic acid is a chelating agent that is used in endodontics to remove inorganic mineral to aide in negotiating calcified canals. What else does it help to do in canal prep?",
        "options": [
            "Removes potassium ions to make tooth less sensitive post op",
            "Removes the inorganic portion of the smear layer",
            "Removes the organic portion of the smear layer",
            "Kills bacteria and digests organic debris"
        ],
        "correct_answer": "Removes the inorganic portion of the smear layer"
    },
    {
        "question": "When using EDTA, one must factor in which variables to evaluate its effectiveness:",
        "options": [
            "Time of application",
            "PH",
            "Concentration",
            "Location of EDTA - coronal/middle/apical third of root canal",
            "All the above"
        ],
        "correct_answer": "All the above"
    },
    {
        "question": "Which of the following is not a step as part of the technique for a shallow (partial) pulpotomy?",
        "options": [
            "Rubber dam isolation",
            "Pulp tissue removed to about 2 mm below the exposure",
            "Use of a large round carbide bur in the slow-speed handpiece to remove tissue",
            "Restoration of the cavity with a hard-setting cement"
        ],
        "correct_answer": "Use of a large round carbide bur in the slow-speed handpiece to remove tissue"
    },
    {
        "question": "With a Cvek pulpotomy, a one to two millimeter deep cavity is prepared into the pulp with a slow speed bur. The material in the pulpal cavity and all dentinal tubules are covered by calcium hydroxide.",
        "options": [
            "Both statements are true.",
            "The first statement is true and the second statement is false.",
            "The first statement is false and the second statement is true.",
            "Both statements are false."
        ],
        "correct_answer": "The first statement is false and the second statement is true."
    },
    {
        "question": "A 9 yo presents to your office with fractured crowns #8 and 9, due to an elbow to the mouth while wrestling with his brother about an hour ago. He is suffering a pain scale of 7/10 when he smiles, drinks or tries to talk. Radiographic and clinical exam reveal exposed pulps and immature apices on both teeth. What is your treatment of choice for the best prognosis?",
        "options": [
            "Immediate extraction and implants #8 and 9.",
            "Direct pulp cap with calcium hydroxide with composite restorations",
            "Cvek or partial pulpotomy with composite restorations.",
            "Pulpectomy to alleviate pain today and NSCRT #8 and 9 at the next appointment."
        ],
        "correct_answer": "Cvek or partial pulpotomy with composite restorations."
    },
    {
        "question": "A differential diagnosis for failure of a NSRCT include all of the following except?",
        "options": [
            "Perforation",
            "Root canal missed",
            "Periodontal disease",
            "Split tooth",
            "Having a proper apical seal"
        ],
        "correct_answer": "Having a proper apical seal"
    },
    {
        "question": "What is the most consistently reported organism found in failed endodontic procedures?",
        "options": [
            "Streptoccocus mutans",
            "Enterococcus faecalis",
            "Propionibacterium",
            "Actinomycoses"
        ],
        "correct_answer": "Enterococcus faecalis"
    },
    {
        "question": "The most common cause of vertical root fractures may be:",
        "options": [
            "Occlusal prematurities",
            "Parafunctional activities",
            "Physical trauma",
            "Iatrogenic dentistry"
        ],
        "correct_answer": "Iatrogenic dentistry"
    },
    {
        "question": "Which of the following represents the most likely location of a second MB canal when accessing a maxillary first molar?",
        "options": [
            "The canal orifice is generally located slightly buccal to or directly on a line between the primary MB canal and distal orifices.",
            "The canal orifice is generally located directly distal to the MB canal orifice.",
            "The canal orifice is generally located mesial to or directly on a line between the primary MB canal and palatal orifices.",
            "The canal orifice is generally located equidistant between all three canals in the central pulpal floor."
        ],
        "correct_answer": "The canal orifice is generally located mesial to or directly on a line between the primary MB canal and palatal orifices."
    },
    {
        "question": "All of the following may be indicative of multiple canals in a maxillary second premolar, EXCEPT",
        "options": [
            "Sharp change in canal density - \"fast break\"",
            "Canal is well centered in root",
            "Root outline unclear",
            "Root has unusual contour",
            "Root differs from expected appearance"
        ],
        "correct_answer": "Canal is well centered in root"
    },
    {
        "question": "All of the following are true concerning the canal configuration of mandibular incisors, EXCEPT?",
        "options": [
            "One canal/one foramen 58.6%",
            "Two canals present 41.4%",
            "With two canals present - Weine Type II 40.1%",
            "With two canals present - Weine Type III 40.1%",
            "With two canals present - Weine Type III 1.3%"
        ],
        "correct_answer": "With two canals present - Weine Type III 40.1%"
    },
    {
        "question": "What antibiotics are commonly used as a scaffold for pulpal revascularization of an immature necrotic permanent tooth?",
        "options": [
            "Cipro",
            "Metronidazole",
            "Ceflor",
            "All the above"
        ],
        "correct_answer": "All the above"
    },
    {
        "question": "What is the major component of gutta percha obturation material?",
        "options": [
            "Gutta-Percha",
            "Zinc Oxide",
            "Heavy Metal Salts",
            "Waxes"
        ],
        "correct_answer": "Zinc Oxide"
    },
    {
        "question": "Zinc Oxide comprises of 59-79% of the gutta percha. Gutta percha itself comprises of 19-20% and the rest are heavy metal salts (1-17%) and waxes or resins (1-4%). Which of the following is NOT a solvent used in removing gutta percha in endodontic retreatment?",
        "options": [
            "Chloroform and methylchloroform",
            "Eucalyptol",
            "Tetrachloroethylene (EndoSolv-E)",
            "Ethylene Chloride",
            "Rectified turpentine"
        ],
        "correct_answer": "Ethylene Chloride"
    },
    {
        "question": "Which of the following does not regulate/effect the setting of zinc oxide eugenol cements?",
        "options": [
            "Particle size of the zinc oxide",
            "PH",
            "Presence of Ca(OH)2 remaining in the canal",
            "Presence of water",
            "Remnants of pulpal tissues"
        ],
        "correct_answer": "Remnants of pulpal tissues"
    },
    {
        "question": "Which of the following is not a suggested use for the material MTA?",
        "options": [
            "Pulp capping",
            "Non surgical apical closure",
            "Perforation repair",
            "Obturation of accessory canals",
            "Surgical root-end filling"
        ],
        "correct_answer": "Obturation of accessory canals"
    },
    {
        "question": "Cvek has shown that with pulp exposures:",
        "options": [
            "It doesn't matter whether the exposure is traumatic or carious, the amount of pulp that is removed is the same",
            "In an traumatic injury, only a few millimeters of pulp tissue needs to be removed, regardless of lapsed time or the size of the exposure",
            "The instrument of choice for tissue removal is a round carbide bur, using a high-speed handpiece and adequate water cooling",
            "The instrument of choice for tissue removal is a round carbide bur, using a slow-speed handpiece and progressing slowly, as to not remove unnecessary healthy pulp tissue"
        ],
        "correct_answer": "In an traumatic injury, only a few millimeters of pulp tissue needs to be removed, regardless of lapsed time or the size of the exposure"
    },
    {
        "question": "Which of the following represents the correct technique when performing a Cvek pulpotomy?",
        "options": [
            "Coronal pulp tissue should be removed to the level of the canal orifice(s).",
            "The most superficial 1mm of coronal pulp only should be excavated.",
            "A pulp cap only is performed with either calcium hydroxide or MTA, as no attempt should be made to remove any coronal pulp tissue.",
            "A 1- to 2-mm deep cavity is prepared into the coronal pulp tissue, and extended deeper as necessary to achieve appropriate hemostasis."
        ],
        "correct_answer": "A 1- to 2-mm deep cavity is prepared into the coronal pulp tissue, and extended deeper as necessary to achieve appropriate hemostasis."
    },
    {
        "question": "NiTi wires have the following properties except:",
        "options": [
            "Superelasticity",
            "Can exist in more than one crystal structure",
            "Poor shape memory",
            "Shape memory"
        ],
        "correct_answer": "Poor shape memory"
    },
    {
        "question": "F. All the above are true F. All the above are true Which is true regarding a pulpotomy in permanent teeth and in primary teeth?",
        "options": [
            "The calcium hydroxide pulpotomy technique is recommended in the treatment of permanent teeth with carious pulp exposure",
            "Formocresol is the medicament of choice for a pulpotomy in permanent teeth",
            "Pulpotomy technique for primary teeth involves only partial removal of the pulp chamber",
            "If there is evidence of hyperemia after the removal of the coronal pulp, formocresol should be placed directly on the pulp stump for hemorrhage control"
        ],
        "correct_answer": "The calcium hydroxide pulpotomy technique is recommended in the treatment of permanent teeth with carious pulp exposure"
    },
    {
        "question": "Which of the following is true about the actions of a formocresol pulpotomy",
        "options": [
            "Formocresol pulpotomies do not produce dentinal bridging",
            "Formocresol pulpotomies contain four zones of fixation.",
            "Formocresol pulpotomies are initiated when the inflammation has spread into the tissues within the root canal.",
            "All of the above are true"
        ],
        "correct_answer": "Formocresol pulpotomies do not produce dentinal bridging"
    },
    {
        "question": "A 3 year old patient has gross decay & early childhood caries in #K and you have to extract it, which appliance would be best to maintain the space?",
        "options": [
            "Distal shoe",
            "Lip bumper",
            "Nance appliance",
            "Lower lingual holding arch"
        ],
        "correct_answer": "Distal shoe"
    },
    {
        "question": "Which of the following two classes of medications should be avoided for anxiolysis in patients with asthma?",
        "options": [
            "Benzodiazepines",
            "Barbiturates",
            "Anti psychotics",
            "Narcotics",
            "Barbiturates"
        ],
        "correct_answer": "Narcotics"
    },
    {
        "question": "What should a practitioner be aware of and treat when uprighting a molar?",
        "options": [
            "Patient sensitivity",
            "Occlusion",
            "Increased probing depths",
            "Damage to adjacent teeth"
        ],
        "correct_answer": "Occlusion"
    },
    {
        "question": "What is the primary indication for a supracrestal fibrotomy?",
        "options": [
            "To reduce the tendency for crowded incisors to relapse",
            "To reduce the possibility for a severely rotated tooth (teeth) to relapse",
            "Both a and b",
            "Neither a or b"
        ],
        "correct_answer": "To reduce the possibility for a severely rotated tooth (teeth) to relapse"
    },
    {
        "question": "Which of the following is not an indication for treating a high frenum?",
        "options": [
            "A high frenum attachment that is associated with an area of persistent gingival inflammation that has not responded to root planning and good oral hygiene.",
            "A frenum that is associated with an area of recession that is progressive.",
            "A high maxillary frenum with a sufficient band of attached gingiva.",
            "A high maxillary frenum and an associated midline diastema that persists after complete eruption of the permanent canines."
        ],
        "correct_answer": "A high maxillary frenum with a sufficient band of attached gingiva."
    },
    {
        "question": "Tanaka and Johnston used the width of the lower incisors to predict the size of what unerupted teeth?",
        "options": [
            "Maxillary Canines and Premolars",
            "Mandibular Canines and Premolars",
            "Maxillary and Mandibular Canines and Premolars",
            "Maxillary and Mandibular Incisors and Canines"
        ],
        "correct_answer": "Maxillary and Mandibular Canines and Premolars"
    },
    {
        "question": "In a mixed dentition analysis using either Moyers or Tanaka-Johnson techniques, which of the following statements is false?",
        "options": [
            "Using the Moyers analysis, the M-D width of the lower incisors is measured and this number is used to predict the size of both the lower and upper unerupted canines and premolars.",
            "With the Tanaka-Johnston analysis, you take ½ the M-D widths of the lower four incisors and add 10.5 to estimate the width of the mandibular canine and premolars for one quadrant",
            "With the Tanaka-Johnston analysis, you take ½ the M-D widths of the lower four incisors and add 10 to estimate the width of the mandibular canine and premolars for one quadrant",
            "With the Tanaka-Johnston analysis, you take ½ the M-D widths of the lower four incisors and add 11 to estimate the width of the maxillary canine and premolars for one quadrant"
        ],
        "correct_answer": "With the Tanaka-Johnston analysis, you take ½ the M-D widths of the lower four incisors and add 10 to estimate the width of the mandibular canine and premolars for one quadrant"
    },
    {
        "question": "Which is true regarding leeway space?",
        "options": [
            "The leeway space in the maxilla is larger than in the mandible",
            "Leeway space is the difference between the mesiodistal widths of the primary canine, first and second primary molars and the permanent canine, first and second premolars",
            "The most favorable dental arch pattern is one in which leeway space is not excessive",
            "The leeway space per side is about 1.5mm in the lower arch and 1.0mm in the upper arch"
        ],
        "correct_answer": "Leeway space is the difference between the mesiodistal widths of the primary canine, first and second primary molars and the permanent canine, first and second premolars"
    },
    {
        "question": "The primate space in the maxilla is between the primary canine and primary first molar. The primate space in the mandible is between the primary canine and primary lateral incisor.",
        "options": [
            "Both statements are true.",
            "The first statement is true. The second statement is false.",
            "The first statement is false. The second statement is true.",
            "Both statements are false."
        ],
        "correct_answer": "Both statements are false."
    },
    {
        "question": "Which of the following statements regarding developing primary dentition is INCORRECT?",
        "options": [
            "Spaced primary arches generally produced favorable alignment of permanent incisors, whereas 80% of arches without spacing produced crowded anterior segments.",
            "Straight terminal plane with primate space allows proper class one permanent molar occlusion with an early mesial shift.",
            "Mesial step will most likely to allow for class I molar occlusion with a late mesial shift.",
            "Distal step is abnormal and is indicative of a developing class II malocclusion."
        ],
        "correct_answer": "Spaced primary arches generally produced favorable alignment of permanent incisors, whereas 80% of arches without spacing produced crowded anterior segments."
    },
    {
        "question": "Biomechanical overload in the pathologic range may enhance root resorption by the following mechanisms EXCEPT?",
        "options": [
            "Production of catabolic cytokines in the PDL",
            "Release of acid from the compressed bone",
            "Damage to the protective cementum layer, resulting in the exposure of dentin",
            "Inhibition of reparative cementum formation"
        ],
        "correct_answer": "Release of acid from the compressed bone"
    },
    {
        "question": "What is the sequence of decay on primary teeth (early childhood caries)?",
        "options": [
            "Maxillary anterior teeth, the maxillary and mandibular first primary molars, and the mandibular canines. The mandibular incisors are usually unaffected.",
            "Maxillary anterior teeth, the mandibular incisor teeth, and the maxillary and mandibular first primary molars. The mandibular canines are unaffected.",
            "Maxillary incisor teeth, the maxillary and mandibular second primary molars, and the mandibular canines. The mandibular anterior teeth are usually unaffected.",
            "Maxillary and mandibular first primary molars, the mandibular anterior teeth, the maxillary incisors, and the maxillary and mandibular second primary molars. The maxillary canines are usually unaffected."
        ],
        "correct_answer": "Maxillary anterior teeth, the maxillary and mandibular first primary molars, and the mandibular canines. The mandibular incisors are usually unaffected."
    },
    {
        "question": "Which of the following is an indication for a lower lingual holding arch?",
        "options": [
            "Loss of Maxillary primary molars",
            "Loss of Mandibular second primary molars",
            "Loss of first maxillary primary molar",
            "Loss of first mandibular primary molar"
        ],
        "correct_answer": "Loss of Mandibular second primary molars"
    },
    {
        "question": "Which of the following represents the most commonly recommended management approach for treated intruded primary teeth?",
        "options": [
            "Initiate immediate, forced eruption of the primary tooth to ensure minimal subsequent occlusal discrepancy.",
            "Perform immediate extraction of the tooth.",
            "Observation initially; with few exceptions, no attempt should be made to reposition the tooth after the accident.",
            "Initiate pulpal debridement, followed by orthodontic eruption at 7-10 days."
        ],
        "correct_answer": "Observation initially; with few exceptions, no attempt should be made to reposition the tooth after the accident."
    },
    {
        "question": "Which statement is true concerning space management in the primary maxillary incisor region?",
        "options": [
            "Space closure rarely occurs in the primary maxillary anterior region when primary incisors are lost",
            "The indication for replacing lost primary maxillary incisors is for cosmetic purposes only",
            "Spacing of maxillary primary anterior teeth is an indication for space maintenance",
            "No previous spacing is an indication for space maintenance in the primary anterior region"
        ],
        "correct_answer": "No previous spacing is an indication for space maintenance in the primary anterior region"
    },
    {
        "question": "Which of the following is not true regarding ectopic eruption of the first permanent molar?",
        "options": [
            "Ectopically erupting molars will erupt into their normal position in 66% of the time",
            "Ectopic eruption occurs more often in boys",
            "Ectopic eruption can be corrected by the Humphrey or Halterman's technique",
            "Ectopic eruption occurs more often in the mandible"
        ],
        "correct_answer": "Ectopic eruption occurs more often in the mandible"
    },
    {
        "question": "The bionator is the most commonly used removable function appliance because of its simplicity, patient acceptance, and use in TMD problems. It is often used for the full correction of a class II malocclusion.",
        "options": [
            "Both statements are true.",
            "The first statement is true. The second statement is false.",
            "The first statement is false. The second statement is true.",
            "Both statements are false."
        ],
        "correct_answer": "The first statement is true. The second statement is false."
    },
    {
        "question": "A tooth is fractured 1mm below the height of the alveolar crest. Forced eruption is planned to expose sound tooth structure for future crown. What is the minimum amount of extrusion that should be accomplished?",
        "options": [
            "1mm",
            "2mm",
            "3mm",
            "4mm"
        ],
        "correct_answer": "4mm"
    },
    {
        "question": "The sella-nasion-subspinale angle (SNA) relates the relative horizontal position of the maxilla to:",
        "options": [
            "The cranial base",
            "Fankfort horizontal",
            "The mandibular plane",
            "The occlusal plane",
            "The prime meridian"
        ],
        "correct_answer": "The cranial base"
    },
    {
        "question": "Which of the following films would be most helpful in viewing the orbit:",
        "options": [
            "Lateral Ceph",
            "Reverse Towne",
            "Oblique body",
            "Waters",
            "Panoramic"
        ],
        "correct_answer": "Waters"
    },
    {
        "question": "What is/are the technique(s) to capture a sialolith on a radiograph?",
        "options": [
            "Lateral Ceph with cheek blown out",
            "Occlusal-over-the-shoulder projection",
            "Anteriorposterior -with cheek blown out",
            "A and B",
            "B and C"
        ],
        "correct_answer": "B and C"
    },
    {
        "question": "How often should biologic monitoring of an approved sterilizer be performed?",
        "options": [
            "Upon each sterilization cycle",
            "Once per month",
            "Periodic observation- at least weekly",
            "Twice per year"
        ],
        "correct_answer": "Periodic observation- at least weekly"
    },
    {
        "question": "Sharpness (decrease of penumbra) is maximized when:",
        "options": [
            "The source-object distance is increased",
            "The source-object distance is increased and the object film distance is decreased",
            "The object-film distance is increased",
            "The object-film distance is decreased"
        ],
        "correct_answer": "The source-object distance is increased and the object film distance is decreased"
    },
    {
        "question": "between tissues.",
        "options": [
            "Due to the inherent high contrast resolution of CT, differences between tissues that differ in physical density by less than 5% can be distinguished"
        ],
        "correct_answer": "Due to the inherent high contrast resolution of CT, differences between tissues that differ in physical density by less than 5% can be distinguished"
    },
    {
        "question": "CBCT technology has been applied in all areas of dentistry except:",
        "options": [
            "Soft tissue analysis",
            "Localization of the inferior alveolar canal",
            "Temporomandibular joint analysis",
            "B and C only"
        ],
        "correct_answer": "Soft tissue analysis"
    },
    {
        "question": "CT Numbers, also called Hounsfield units are scaled in cortical bone at which of the following numbers?",
        "options": [
            "+2000",
            "+1000",
            "+100",
            "0"
        ],
        "correct_answer": "+1000"
    },
    {
        "question": "Cone beam CT can be used in dentistry for all the following application, except",
        "options": [
            "Locate the precise position of impacted teeth",
            "3-D airway analysis of obstructive sleep apnea and adenoids",
            "Diagnosis of TMJ disorders by precisely mapping muscles and their attachments.",
            "Assess the osseous dimensions, bone density, and alveolar height, especially when multiple implants are planned"
        ],
        "correct_answer": "Diagnosis of TMJ disorders by precisely mapping muscles and their attachments."
    },
    {
        "question": "\"Scatter\" on a CBCT image is caused by:",
        "options": [
            "Very dense objects",
            "Objects with low density",
            "Both",
            "Neither"
        ],
        "correct_answer": "Very dense objects"
    },
    {
        "question": "Which of the following is not one of the four components to CBCT image acquisition?",
        "options": [
            "X-ray generation",
            "Image detection system",
            "Image reconstruction",
            "Image display",
            "Image transduction"
        ],
        "correct_answer": "Image transduction"
    },
    {
        "question": "Which of the following is (are) false relative to Cone Beam CT? 1. Field of view is synonymous with scan volume 2. The speed with which individual images are acquired is called the frame rate and is measured in frames, projected images, per second. 3. The ability of CBCT to display differences in attenuation is related to the ability of the detector to detect subtle contrast difference. This parameter is called the bit depth of the system and determines the number of shades of gray available to display the attenuation. 4. Once the basis projection frames have been acquired, it is necessary to process these data to create the volumetric data set. This process is called primary reconstruction.",
        "options": [
            "1 and 2",
            "1 and 3",
            "2 and 3",
            "4 only",
            "None of the above"
        ],
        "correct_answer": "None of the above"
    },
    {
        "question": "Which of the following is incorrect when comparing a cone-beam CT (CBCT) to a conventional CT?",
        "options": [
            "Compared with conventional CT, the time for CBCT scanning is substantially reduced.",
            "Relative to conventional CT, the radiation dose for CBCT is significantly less.",
            "Relative to conventional CT, the scanning process is faster for CBCT.",
            "Compared with conventional CT, the financial burden for CBCT is significantly more expensive."
        ],
        "correct_answer": "Compared with conventional CT, the financial burden for CBCT is significantly more expensive."
    },
    {
        "question": "Which of the following statement(s) is/are advantages of Computed Tomographic (CT) imaging over conventional film radiography and tomography?",
        "options": [
            "Because of the inherent high-contrast resolution of CT, differences between tissues that differ in physical density by less than 1% can be distinguished",
            "It eliminates the superimposition of images of structures outside the area of interest.",
            "As compared with plain-film radiography, CT involves much higher doses of radiation, resulting in a marked increase in radiation exposure in the population.",
            "Data from a single CT imaging procedure can be viewed as images in 3 dimensions, the axial, coronal, or sagittal planes, depending on the diagnostic task.",
            "A,B, D"
        ],
        "correct_answer": "A,B, D"
    },
    {
        "question": "When using surface disinfectants, one must keep in mind all of the following EXCEPT:",
        "options": [
            "Ortho-phthala-dehyde (OPA) is classified as an intermediate level disinfectant and is an alternative to those with glutaraldehyde sensitivities",
            "Glutaraldehyde is classified as a high level disinfectant and can be used as a liquid sterilant with sufficient immersion time.",
            "Chorine dioxide is an effective rapid acting environmental surface disinfectant (3 minutes) or chemical sterilant (6 hours)",
            "Alcohols are not effective in the presence of blood and saliva, evaporate quickly and are damaging to certain materials such as plastics and vinyl"
        ],
        "correct_answer": "Ortho-phthala-dehyde (OPA) is classified as an intermediate level disinfectant and is an alternative to those with glutaraldehyde sensitivities"
    },
    {
        "question": "What in not an appropriate active ingredient to use for intermediate level work surface infection control?",
        "options": [
            "Quaternary ammonium chloride",
            "Iodophors",
            "Phenols",
            "Halogens such as chlorine or iodine"
        ],
        "correct_answer": "Quaternary ammonium chloride"
    },
    {
        "question": "A disinfection procedure that inactivates vegetative bacteria, mycobacteria, fungi, viruses, and not necessarily high numbers of bacterial spores.",
        "options": [
            "High-Level Disinfectant",
            "Medium-Level Disinfectant",
            "Low-Level Disinfectant",
            "Hospital-Level Disinfectant"
        ],
        "correct_answer": "High-Level Disinfectant"
    },
    {
        "question": "Generally, semi-critical items require what type of disinfection?",
        "options": [
            "High-level disinfection with the use of wet pasteurization or chemical germicides, such as Glutaraldehyde (Cidex), stabilized hydrogen peroxide, chlorine and chlorine compounds for ≥ 20 min exposure time",
            "Intermediate-level disinfection, such as ethyl or isopropyl alcohol (70% to 90%), Phenolic or iodophor germicidal detergent for ≤10 min exposure time",
            "Low-level disinfection, such as sodium hypochlorite, Phenolic, iodophor or quarternary ammonium germicidal detergent for ≥ 10 min exposure time",
            "None of the above"
        ],
        "correct_answer": "High-level disinfection with the use of wet pasteurization or chemical germicides, such as Glutaraldehyde (Cidex), stabilized hydrogen peroxide, chlorine and chlorine compounds for ≥ 20 min exposure time"
    },
    {
        "question": "The maximum amount of CFU's allowed in dental unit water lines by the EPA is:",
        "options": [
            "500",
            "5,000",
            "50,000",
            "500,000"
        ],
        "correct_answer": "500"
    },
    {
        "question": "The major causes of facial fractures include falls and sports-related activities. The most common place for a mandible to fracture is in the angle of the mandible (29.1% of the time).",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "The first statement is true, and the second statement is false",
            "The first statement is false, and the second statement is true"
        ],
        "correct_answer": "Both statements are false"
    },
    {
        "question": "You just took a radiograph, but do not like the contrast. For short scale, how can you increase contrast and maintain original density?",
        "options": [
            "Decrease the original kVp by 15 kVp; Use 2 times the original exposure time.",
            "Increase the original kVp by 15 kVp; Use one half the original exposure time.",
            "Increase the original kVp by 15 kVp; Use 2 times the original exposure time.",
            "Decrease the original kVp by 15 kVp; Use one half the original exposure time."
        ],
        "correct_answer": "Decrease the original kVp by 15 kVp; Use 2 times the original exposure time."
    },
    {
        "question": "When interpreting panoramic films, all are true of ghost images EXCEPT:",
        "options": [
            "May obscure normal anatomy or be mistaken for pathologic conditions",
            "Results when the x-ray beam projects through a dense object (earring/spinal column/ramus) that is in the path of the x-ray beam but out of the portion of the focal trough being imaged",
            "Results in a projection on the same side of the radiograph with a reversed configuration",
            "Object typically appears blurred and projects over the midline structures"
        ],
        "correct_answer": "Results in a projection on the same side of the radiograph with a reversed configuration"
    },
    {
        "question": "You are examining a panoramic radiograph. The occlusal plane on the radiograph appears flat or inverted and the image on the mandible is distorted. What would be the cause of this?",
        "options": [
            "The patient's chin is placed too high.",
            "The patient's chin is placed too low.",
            "The patient is positioned too far posterior.",
            "The patient is positioned too far anterior."
        ],
        "correct_answer": "The patient's chin is placed too high."
    },
    {
        "question": "A person has a positive Hepatitis B surface and core antibodies but is negative for the surface antigen. The patient has a(n)",
        "options": [
            "Chronic Hepatitis B infection",
            "Acute Hepatitis B Infection",
            "Immunity from Natural Infection",
            "Immunity from Vaccination"
        ],
        "correct_answer": "Immunity from Natural Infection"
    },
    {
        "question": "Which of the following statement regarding Hep B vaccines is TRUE?",
        "options": [
            "Dose 1 and 2 should be given 2 months apart",
            "Dose 3 should be given 3 months after the 2nd dose",
            "Antibody response to hepatitis B surface antigen should be performed 1-2 months after the third vaccine dose",
            "Booster dose should be given every 10 years."
        ],
        "correct_answer": "Antibody response to hepatitis B surface antigen should be performed 1-2 months after the third vaccine dose"
    },
    {
        "question": "All of the following are RNA viruses except?",
        "options": [
            "HAV",
            "HBV",
            "HCV",
            "HDV",
            "HEV"
        ],
        "correct_answer": "HBV"
    },
    {
        "question": "Regarding the ADC (analog-to-digital conversion) process in digital radiography, sampling means _______ and narrow sampling ____________",
        "options": [
            "A small range of voltage values are grouped together as a single value; mimics the original signal but leads to larger memory requirements for the resulting digital image",
            "A large range of voltage values are grouped together as a signal value; mimics the original signal and does not require a lot of memory for the resulting digital image",
            "A small range of voltage values in multiple values; replicates a previous captured signal and leads to larger memory requirements for the resulting digital image",
            "A large range of voltage values in multiple values; replicates a previous captured signal and leads to larger memory requirements for the resulting digital image"
        ],
        "correct_answer": "A small range of voltage values are grouped together as a single value; mimics the original signal but leads to larger memory requirements for the resulting digital image"
    },
    {
        "question": "Which of the following represents the image of choice for soft-tissue assessment of the TMJ?",
        "options": [
            "Cone-beam CT",
            "Magnetic Resonance Imaging (MRI)",
            "Conventional CT",
            "Arthrography"
        ],
        "correct_answer": "Magnetic Resonance Imaging (MRI)"
    },
    {
        "question": "In diagnosing condylar neck fractures with suspected medial displacement, panoramic views must be supplemented with a _______________.",
        "options": [
            "Water's view",
            "Towne's view",
            "Posterior-Anterior radiograph",
            "Lateral Oblique radiograph"
        ],
        "correct_answer": "Towne's view"
    },
    {
        "question": "Regarding tuberculosis, all of the following statements are considered true except?",
        "options": [
            "With active sputum positive TB, urgent care only; palliate urgent problems with medication if contained facility in hospital environment not available",
            "INH and rifampin therapy can cause nephrotoxicity and elevations of serum aminotransferases",
            "With active sputum positive TB, urgent care requiring use of hand-piece performed only in hospital setting with isolation, sterilization (gloves/mask/gown), and special ventilation",
            "When patient produces consistently negative sputum, treat as normal patient (noninfectious)"
        ],
        "correct_answer": "INH and rifampin therapy can cause nephrotoxicity and elevations of serum aminotransferases"
    },
    {
        "question": "Xerostomic drugs include:",
        "options": [
            "Antidepressant and sediative/hypnotic",
            "Antidepressant, sediative/hypnotic, antiparkinson agent",
            "Antihistamine, antidepressant, sediative/hypnotic, antiparkinson agent",
            "Proton pump inhibitor, antihistamine, antidepressant, sediative/hypnotic, antiparkinson agent"
        ],
        "correct_answer": "Proton pump inhibitor, antihistamine, antidepressant, sediative/hypnotic, antiparkinson agent"
    },
    {
        "question": "Which of the following salivary stimulants is approved by the FDA to be used for the relief of xerostomia?",
        "options": [
            "Bromhexine, Pilocarpine HCL",
            "Pilocarpine HCL, Cevimeline HCL",
            "Cevimeline HCL , Anetholetrithione",
            "Bromhexine, Anetholetrithione"
        ],
        "correct_answer": "Pilocarpine HCL, Cevimeline HCL"
    },
    {
        "question": "A squamous cell carcinoma that was discovered on the lateral border of the tongue during routine oral cancer screening was biopsied and found to be in Stage II category after excisional biopsy. Patient is concerned with his survival rate. What do you tell him?",
        "options": [
            "5 year survival rate is 100% because it was completely removed in the biopsy",
            "5 year survival rate is about 66% due to its stage",
            "5 year survival rate is unknown due to the high recurrence rate",
            "5 year survival rate is about 9% due to its stage"
        ],
        "correct_answer": "5 year survival rate is about 66% due to its stage"
    },
    {
        "question": "The 5-year survival rate of oral SCC is approximately:",
        "options": [
            "10%",
            "23%",
            "57%",
            "76%"
        ],
        "correct_answer": "57%"
    },
    {
        "question": "What complication can be commonly seen in the infant at birth if codeine is taken during the third trimester?",
        "options": [
            "Cleft palate",
            "Heart murmur",
            "Breathing difficulties",
            "Spina Bifida"
        ],
        "correct_answer": "Breathing difficulties"
    },
    {
        "question": "Which of the following is the most common clinically significant odontogenic tumor?",
        "options": [
            "Calcifiying epithelial odontogenic tumor",
            "Ameloblastic fibroma",
            "Ameloblastic fibro-odontoma",
            "Ameloblastoma"
        ],
        "correct_answer": "Ameloblastoma"
    },
    {
        "question": "Which of the following may present as a radiopaque lesion associated with the root of a non-vital tooth?",
        "options": [
            "Cementoblastoma",
            "Focal sclerosing osteomyelitis",
            "Periapical cemento-osseous dysplasia",
            "Idiopathic osteosclerosis"
        ],
        "correct_answer": "Focal sclerosing osteomyelitis"
    },
    {
        "question": "Choose the correct statement that best describes pemphigoid and/or pemphigus?",
        "options": [
            "Pemphigoid alters the cellular connections at the basement membrane (desmosomes)",
            "Positive Nikolsky sign is seen in pemphigus and pemphigoid",
            "Pemphigus rarely affects the oral cavity",
            "Pemphigus alters the cellular connections above the basement membrane (hemidesmosomes)",
            "Pemphigoid rarely affects the oral cavity"
        ],
        "correct_answer": "Pemphigoid rarely affects the oral cavity"
    },
    {
        "question": "In regards to screening tests for pre-op evaluation of bleeding times, which statement is incorrect?",
        "options": [
            "PT (prothrombin time) is activated by tissue thromboplastin, tests extrinsic and common pathways, with a normal time of 11-15 seconds",
            "PT measures factors II, III, V, VII, and X",
            "APTT (activated partial thromboplastin time) tests intrinsic and common pathways, with a normal reading of 25-35 seconds",
            "INR (International normalized ratio) has normal range of .8-1.2 and is calculated by the ratio of the patients PT/normal PT raised to the power of the ISI (International sensitivity index)"
        ],
        "correct_answer": "PT measures factors II, III, V, VII, and X"
    },
    {
        "question": "What is acute sialadenitis?",
        "options": [
            "Acute infection of the submandibular gland caused by staphylococcus aureus",
            "Acute infection of the parotid gland caused by three viruses: Mumps, Group A Coxsackievirus, Cytomegalovirus",
            "Acute bacterial infection of the major salivary glands that is caused by the presence of salivary stone"
        ],
        "correct_answer": "Acute infection of the parotid gland caused by three viruses: Mumps, Group A Coxsackievirus, Cytomegalovirus"
    },
    {
        "question": "Necrotizing sialometaplasia is a self limiting neoplastic inflammatory condition of unknown etiology. Treatment is via anti-virals.",
        "options": [
            "Both statements are true.",
            "The first statement is true. The second statement is false.",
            "The first statement is false. The second statement is true.",
            "Both statements are false."
        ],
        "correct_answer": "The first statement is true. The second statement is false."
    },
    {
        "question": "Human papilloma virus is associated with all the following lesions Except",
        "options": [
            "Verruca vulgaris",
            "Condyloma Acuminatum",
            "Focal Epithelial Hyperplasia",
            "Verruciform Xanthoma",
            "Squamous papilloma"
        ],
        "correct_answer": "Verruciform Xanthoma"
    },
    {
        "question": "Assuming that a patient that is taking corticosteroids meets the requirements for supplementation, the patient should receive which of the following to prevent an adrenal insufficiency?",
        "options": [
            "No additional therapy",
            "Normal morning dose, supplemental pre and intraoperatively to achieve 100mg equivalent during the 1st hour of surgery and 25mg every 8 hrs for 24-48hrs post operatively.",
            "Double the morning dose, supplemental pre and intraoperatively to achieve 200mg equivalent during the 1st hour of surgery and 50mg every 8 hrs for 24-48hrs post operatively.",
            "Skip the morning dose, supplemental pre and intraoperatively to achieve 100mg equivalent during the 1st hour of surgery and 25mg every 4 hrs for 72-96hrs post operatively."
        ],
        "correct_answer": "Normal morning dose, supplemental pre and intraoperatively to achieve 100mg equivalent during the 1st hour of surgery and 25mg every 8 hrs for 24-48hrs post operatively."
    },
    {
        "question": "Limiting the epinephrine given to a patient with hyperthyroidism is wise because excessive epinephrine may lead to?",
        "options": [
            "Heart attack",
            "Stroke",
            "Thyrotoxicosis",
            "Aneurysm",
            "Headache"
        ],
        "correct_answer": "Thyrotoxicosis"
    },
    {
        "question": "The reason why the use of epinephrine (and other sympathomimetics) requires special consideration when treating hyperthyroid patients is:",
        "options": [
            "Epinephrine acts on alpha-adrenergic receptors, causing vasodilation",
            "Epinephrine acts on beta-2 receptors causing vasoconstriction",
            "Epinephrine acts on alpha-adrenergic and beta-2 receptors causing vasodilation",
            "Epinephrine acts on beta-2 receptors causing vasodilation and on alpha- adrenergic receptors, causing vasoconstriction"
        ],
        "correct_answer": "Epinephrine acts on beta-2 receptors causing vasodilation and on alpha- adrenergic receptors, causing vasoconstriction"
    },
    {
        "question": "Which of the following dermatologic conditions is classically associated with generalized widening of the periodontal ligament space?",
        "options": [
            "Systemic sclerosis",
            "Ehlers-Danlos syndrome",
            "Tuberous sclerosis",
            "Epidermolysis bullosa"
        ],
        "correct_answer": "Systemic sclerosis"
    },
    {
        "question": "Because nonselective B blockers block B2 adrenergic receptor-mediated vasodilation in peripheral blood vessels, there is a risk of a hypertensive episode after administration of local anesthetic agents that contain vasoconstrictors or the use of epinephrine impregnated retraction cords.",
        "options": [
            "Only the first statement is true",
            "Only the second statement is true",
            "Both statements are true",
            "Both statements are false"
        ],
        "correct_answer": "Both statements are true"
    },
    {
        "question": "In regards to organ transplant procedures, the best clinical results are attained with triple drug immunosuppressive therapy, which includes all of the following except?",
        "options": [
            "Cyclosporine",
            "Rapamycin",
            "Prednisone",
            "Azathioprine"
        ],
        "correct_answer": "Rapamycin"
    },
    {
        "question": "Necrotizing sialometaplasia is:",
        "options": [
            "A reactive, nonneoplastic inflammatory process that usually affects the minor salivary glands of the Palate.",
            "Caused by diminished blood flow to the affected area to include: trauma, local anesthetic injection and smoking.",
            "Often mistaken for malignant carcinoma.",
            "All the above"
        ],
        "correct_answer": "All the above"
    },
    {
        "question": "LH, FSH, and progesterone are produced in the pituitary. High levels of LH and FSH during pregnancy, causes capillary permeability which can make the patients susceptible to such conditions like melasma, gingivitis, gingival hyperplasia, and pyogenic granuloma.",
        "options": [
            "Both statements are true.",
            "The first statement is true. The second statement is false.",
            "The first statement is false. The second statement is true.",
            "Both statements are false"
        ],
        "correct_answer": "The first statement is false. The second statement is true."
    },
    {
        "question": "A patient presents to your clinic coughing with bloody sputum, low-grade fever, enlarged cervical lymph nodes (scrofula) and night sweats. Which drug regimen would be best to treat this patient who has been diagnosed with active tuberculosis?",
        "options": [
            "Isoniazid (INH) for 2 months",
            "Isoniazid (INH) with Rifampin for 3 months",
            "Isoniazid (INH) with rifampin and pyrazinamide for 2 months, followed by INH and rifampin for 4 months",
            "Rifampin for 6 months"
        ],
        "correct_answer": "Isoniazid (INH) with rifampin and pyrazinamide for 2 months, followed by INH and rifampin for 4 months"
    },
    {
        "question": "The superior head of lateral pterygoid originates on the ___________ and inserts on the ___________.",
        "options": [
            "Infratemporal surface and infratemporal crest of the greater wing of the sphenoid bone; articular disc and fibrous capsule of the TMJ.",
            "Lateral surface of the lateral pterygoid plate; neck of condyle of the mandible",
            "Coronoid notch; articular disk",
            "Patella; styloid process"
        ],
        "correct_answer": "Infratemporal surface and infratemporal crest of the greater wing of the sphenoid bone; articular disc and fibrous capsule of the TMJ."
    },
    {
        "question": "A joint sound categorized as grating that is thought to be a sign of disk perforation, disk disruption, or terminal stage osteoarthritis is known as?",
        "options": [
            "Clicking",
            "Popping",
            "Crepitus",
            "Reciprocal clicking"
        ],
        "correct_answer": "Crepitus"
    },
    {
        "question": "In diagnosing disc displacement with reduction, all of the following must be present EXCEPT:",
        "options": [
            "Reproducible joint noise that occurs at variable positions during opening and closing mandibular movements",
            "Soft tissue imaging revealing displaced disc that improves its position during jaw opening, and hard tissue imaging showing an absence of extensive degenerative bone changes",
            "Soft tissue imaging revealing displaced disc that does not improve its position during jaw opening",
            "May be accompanied by pain, and deviation during movement coinciding with a click"
        ],
        "correct_answer": "Soft tissue imaging revealing displaced disc that does not improve its position during jaw opening"
    },
    {
        "question": "Which of the following statements is incorrect about disc dislocation either with or without reduction?",
        "options": [
            "Normally a long history of clicking in the joint and more recently some catching sensation may be seen.",
            "A sudden loud click will be heard recapturing the disc, in which a normal range of mandibular movement will follow in patients diagnosed with disc dislocation with reduction.",
            "Clinical characteristics of disc dislocation without reduction include a range of mandibular opening of 25 to 30 mm, with the mandible deflecting towards the involved joint at the end of movement.",
            "Patients diagnosed with disc dislocation without reduction present with a consistent joint click and a maximum point of opening revealing a soft-end feel."
        ],
        "correct_answer": "Patients diagnosed with disc dislocation without reduction present with a consistent joint click and a maximum point of opening revealing a soft-end feel."
    },
    {
        "question": "A patient with an Anteriorly Displaced Disc without reduction will complain of which of the following?",
        "options": [
            "Severe pain during meals",
            "Occasional popping and clicking without pain",
            "Occasional popping and clicking with pain",
            "Occasional opening and the jaw will \"lock\" in place"
        ],
        "correct_answer": "Occasional opening and the jaw will \"lock\" in place"
    },
    {
        "question": "Hyperparathyroidism can involve all of the radiographic features except one of the following?",
        "options": [
            "Demineralization and thinning of cortical boundaries often occur in the jaws in cortical boundaries such as the inferior border, mandibular canal, and the cortical outlines of the maxillary sinuses",
            "The density of the jaws is decreased, resulting in a radiolucent appearance that contrasts with the density of the teeth",
            "A change in the normal trabecular pattern may occur, resulting in a ground glass appearance of numerous, small, randomly oriented trabeculae",
            "Brown tumors (may resemble a central giant cell granuloma or an aneurysmal bone cyst) occur late in the disease and in about 20% of cases",
            "Depending on the duration and severity of the disease, loss of the lamina dura may occur around one tooth or all the remaining teeth - with the loss being either complete or partial around a particular tooth"
        ],
        "correct_answer": "Brown tumors (may resemble a central giant cell granuloma or an aneurysmal bone cyst) occur late in the disease and in about 20% of cases"
    },
    {
        "question": "The most common location of the Adenomatoid Odontogenic Tumor",
        "options": [
            "Anterior maxillae",
            "Posterior maxillae",
            "Posterior mandible",
            "Midline of the mandible"
        ],
        "correct_answer": "Anterior maxillae"
    },
    {
        "question": "Of all ectopic thyroids, ninety percent are located in/on the______________. Seventy percent of these patients suffer from _________.",
        "options": [
            "Submandibular Gland, Hyperthroidism",
            "Submandibular Gland, Hypothyroidism",
            "Lingual Dorsum, Hyperthyroidism",
            "Lingual Dorsum, Hypothyroidism"
        ],
        "correct_answer": "Lingual Dorsum, Hypothyroidism"
    },
    {
        "question": "Which statement regarding Stevens-Johnson syndrome is true?",
        "options": [
            "It presents with severe ocular blistering, scarring may occur, similar to that in bullous pemphigoid.",
            "The etiology is usually a result of an acute infection rather than a drug reaction",
            "For a diagnosis to be made, either the ocular or genital mucosa should be affected in conjunction with the oral and skin lesions.",
            "A less severe form of erythema multiforme and has an acute onset",
            "All of the above are true"
        ],
        "correct_answer": "For a diagnosis to be made, either the ocular or genital mucosa should be affected in conjunction with the oral and skin lesions."
    },
    {
        "question": "The primary hereditary abnormalities of the enamel that are unrelated to other disorders are termed___________________.",
        "options": [
            "Dentinogenesis Imperfecta",
            "Odontodysplasia",
            "Amelogenesis Imperfecta",
            "Osteogenesis Imperfecta"
        ],
        "correct_answer": "Amelogenesis Imperfecta"
    },
    {
        "question": "Lesions of juvenile fibrous dysplasia should not be treated by radiotherapy due to the risk of what?",
        "options": [
            "Future malignancy",
            "May increase in size",
            "Inhibits healing",
            "Cosmetic scarring"
        ],
        "correct_answer": "Future malignancy"
    },
    {
        "question": "Regarding fissured tongue, which of the following is false?",
        "options": [
            "The prevalence of fissured tongue ranges from 12%-15%",
            "The prevalence and severity appear to increase with age",
            "Fissured tongue also may be a component of Melkersson-Rosenthal syndrome",
            "A hereditary basis has been suggested for geographic tongue, and the same gene or genes may possibly be linked to both fissured and geographic tongue"
        ],
        "correct_answer": "The prevalence of fissured tongue ranges from 12%-15%"
    },
    {
        "question": "Prevelence is 2-5% Which of the following statements is incorrect when comparing geographic tongue and fissured tongue?",
        "options": [
            "Both conditions are typically asymptomatic, although some patients may complain of mild burning or soreness.",
            "A strong association has been found between fissured and geographic tongue, with many patients having both conditions.",
            "Considerable variations of both conditions can be seen upon clinical presentation.",
            "No association is suspected between fissured and geographic tongue, as the clinical presentation represents dissimilar conditions."
        ],
        "correct_answer": "No association is suspected between fissured and geographic tongue, as the clinical presentation represents dissimilar conditions."
    },
    {
        "question": "Which statement (s) is/are true regarding migratory glossitis (geographic tongue)?",
        "options": [
            "Most cases of migratory glossitis occur due to an allergic reaction to oral medicine.",
            "Patients with psoriasis have a higher incidence of migratory glossitis.",
            "Patients with a fissured tongue often have migratory glossitis as well.",
            "B and c"
        ],
        "correct_answer": "B and c"
    },
    {
        "question": "When considering dental management for a patient with congestive heart failure (CHF), all of the following applies except?",
        "options": [
            "Expect patient to be taking one or a combination of the following medications - loop diuretics (Lasix), thiazide diuretics (HCTZ), ACE inhibitors (the ‗prils'), angiotensin receptor blockers (the ‗sartans'), beta blockers (the ‗lols' such as Atenolol), or Digoxin",
            "For patients taking digitalis, avoid epinephrine; but if considered essential - use cautiously (.036mg epinephrine)",
            "You may use nonsteroidal anti-inflammatory drugs (long-term)",
            "You may use nitrous oxide/oxygen sedation"
        ],
        "correct_answer": "You may use nonsteroidal anti-inflammatory drugs (long-term)"
    },
    {
        "question": "Sleep apnea patients tend to:",
        "options": [
            "Snore loudly",
            "Be overweight",
            "Have high blood pressure",
            "Has some physical abnormality in the nose, throat, or other parts of the upper airway",
            "All the above"
        ],
        "correct_answer": "All the above"
    },
    {
        "question": "There has been a bidirectional link between sleep apnea and obesity. There is another bidirectional link between sleep apnea and diabetes mellitus.",
        "options": [
            "Both statements are true.",
            "The first statement is true. The second statement is false.",
            "The first statement is false. The second statement is true.",
            "Both statements are false"
        ],
        "correct_answer": "Both statements are true."
    },
    {
        "question": "Depending on the severity, sleep apnea may be treated by all of the following regimens EXCEPT,",
        "options": [
            "Weight loss to reduce snoring",
            "Sleep aid medication",
            "Nasal decongestion",
            "Positional therapy such as side sleeping and discourage supine sleeping",
            "Positive airway pressure machines, such as CPAP"
        ],
        "correct_answer": "Sleep aid medication"
    },
    {
        "question": "In a RDP, which is NOT an indication for using a bar clasps:",
        "options": [
            "When a small degree of undercut (.01in) exists in the cervical 1/3 of the abutment tooth",
            "On abutment teeth for tooth-supported partial dentures or tooth-supported modification areas",
            "In distal extension base situations",
            "In situations in which esthetic considerations must be accommodated and a cast clasp is indicated.",
            "In an area with a large soft tissue undercut"
        ],
        "correct_answer": "In an area with a large soft tissue undercut"
    },
    {
        "question": "What is the most important factor in RDP design?",
        "options": [
            "Type of metal used",
            "Esthetics",
            "Clasp systems that cause least harm",
            "Minor connectors"
        ],
        "correct_answer": "Clasp systems that cause least harm"
    },
    {
        "question": "Which of the following statements regarding polyvinyl siloxane (PVS) and polyether impression material is false?",
        "options": [
            "PVS is considered an addition silicone and results in no by-product formation upon setting.",
            "Of all commonly used impression materials, PVS is least affected by pouring delays, or by second pours, and is still accurate, even when poured 1 week after removal from the mouth.",
            "Polyether exhibits excellent dimensional stability even when pouring is delayed for longer periods of time- it is accurate when poured 1 week after removal from the mouth.",
            "Polyether is hydrophobic, thus impressions should not be stored in a moist environment in order to prevent dimensional alteration."
        ],
        "correct_answer": "Polyether is hydrophobic, thus impressions should not be stored in a moist environment in order to prevent dimensional alteration."
    },
    {
        "question": "What gas is produced by the setting reaction of polyvinylsiloxanes?",
        "options": [
            "Carbon",
            "Nitrogen",
            "Hydrogen",
            "Oxygen"
        ],
        "correct_answer": "Hydrogen"
    },
    {
        "question": "In regards to the characteristics of various impression materials, all of the following statements are true, except",
        "options": [
            "Setting times, from longest to shortest, is polysulfides > silicones > polyethers",
            "Tear strength, from strongest to weakest, is polysulfides > silicones >polyethers",
            "Alginate has a flexibility of 11-15% where as silicone's flexibility is 5%",
            "Dimensional change for silicone (PVS) is 0.5% over 24 hours"
        ],
        "correct_answer": "Dimensional change for silicone (PVS) is 0.5% over 24 hours"
    },
    {
        "question": "Which of the following elastomeric impression material is ideal for subgingival preps?",
        "options": [
            "Polysulfide",
            "Polyether",
            "Condensation silicone",
            "Addition silicone"
        ],
        "correct_answer": "Polysulfide"
    },
    {
        "question": "Which of the following material is the most dimensional stable?",
        "options": [
            "Reversible Hydrocolloid",
            "Irreversible Hydrocolloid",
            "Addition Silicone",
            "Polysufide"
        ],
        "correct_answer": "Addition Silicone"
    },
    {
        "question": "All the following are proper procedures to disinfect impression material before sending it to the laboratory, EXCEPT",
        "options": [
            "Rinse off blood, saliva and debris",
            "Disinfect impressions using an intermediate-level, EPA-registered disinfectant for the contact time recommended by the manufacturer (usually about 15 minutes)",
            "Immersing in disinfecting agents such as 1% sodium hypochlorite or 2% potentiated glutaraldehyde or iodophors for up to 1 hour",
            "Sometimes soft, camelhair brushes can help remove debris"
        ],
        "correct_answer": "Immersing in disinfecting agents such as 1% sodium hypochlorite or 2% potentiated glutaraldehyde or iodophors for up to 1 hour"
    },
    {
        "question": "Which could not be the cause of generalized pain on an edentulous ridge of a patient wearing a removable prosthesis?",
        "options": [
            "Malocclusion",
            "Excessive OVD",
            "Inaccurate denture base.",
            "Resin spicule"
        ],
        "correct_answer": "Resin spicule"
    },
    {
        "question": "Which statement regarding rest seat design on posterior teeth is INCORRECT?",
        "options": [
            "The occlusal rest seat is triangular, with the base of the triangle located at the marginal ridge and the apex pointing toward the center of the tooth",
            "The angle formed between the floor of the rest seat and the proximal surface should be less than 90 degrees",
            "When cutting rest seat preps, undercuts are more likely when using a round bur, vice a tapered cylinder",
            "Rest seats preps should be completed prior to guide plane preps",
            "Marginal ridge reduction should be at least 1mm and deeper towards the center of the tooth"
        ],
        "correct_answer": "Rest seats preps should be completed prior to guide plane preps"
    },
    {
        "question": "In determination of OVD and dentures, all of the following are possible techniques except?",
        "options": [
            "Silverman - closest speaking space",
            "Pound - Phonetics and Esthetics",
            "Littleman - Neuromuscular perception",
            "Pleasure - pleasure points",
            "Boos: Bimeter"
        ],
        "correct_answer": "Littleman - Neuromuscular perception"
    },
    {
        "question": "When making an impression with irreversible hydrocolloid, which of the following statement is true?",
        "options": [
            "Select the largest try that will fit comfortably in the patient's mouth. A greater bulk of material produces a more accurate impression because it has a more favorable surface are/volume ratio and is less susceptible to water loss or gain.",
            "Select a tight fitting tray in which a uniform thin layer of material is used. This produces the most accurate impression.",
            "For optimum results, the teeth should be cleaned and thoroughly dry.",
            "The tray should be removed by teasing or wiggling 2 to 3 minutes after gelation. This will prevent tearing of the impression material."
        ],
        "correct_answer": "Select the largest try that will fit comfortably in the patient's mouth. A greater bulk of material produces a more accurate impression because it has a more favorable surface are/volume ratio and is less susceptible to water loss or gain."
    },
    {
        "question": "In which of the following situations can an irreversible hydrocolloid NOT be used?",
        "options": [
            "Provisional Crown and Bridge Impression",
            "Study Models",
            "Final Impressions when the prep margin is a chamfer.",
            "All of the above can be impressed."
        ],
        "correct_answer": "All of the above can be impressed."
    },
    {
        "question": "Alginates, if not poured up immediately, will have a tendency to exhibit syneresis, which is defined as",
        "options": [
            "Swelling from absorbing surrounding water",
            "Swelling from absorbing surrounding gases",
            "Distortion due to exudate or liquid released on the surface",
            "Distortion due to hydrogen gas release"
        ],
        "correct_answer": "Distortion due to exudate or liquid released on the surface"
    },
    {
        "question": "The rotation of a tissue-borne RDP during function is directionally around how many axis?",
        "options": [
            "1",
            "2",
            "3",
            "4"
        ],
        "correct_answer": "3"
    },
    {
        "question": "Bilateral edentulous areas located posterior to the natural teeth is what Kennedy classification?",
        "options": [
            "Class I",
            "Class II",
            "Class III",
            "Class IV"
        ],
        "correct_answer": "Class I"
    },
    {
        "question": "Which of the following is true regarding Applegate's Rules for applying the Kennedy Classification?",
        "options": [
            "If a first molar is missing and is not to be replaced, it is not considered in the classification (e.g., if the opposing first molar is likewise missing and is not to be replaced) (Rule 4)",
            "The most posterior edentulous area (or areas) does not determines the classification (Rule 5)",
            "The extent of the modification is not considered, only the number of additional edentulous areas (Rule 7)",
            "There can be modification areas in Class IV arches (Rule 8)"
        ],
        "correct_answer": "The extent of the modification is not considered, only the number of additional edentulous areas (Rule 7)"
    },
    {
        "question": "Which of the following combinations represents a tooth-supported removable partial denture?",
        "options": [
            "Kennedy Class I and II",
            "Kennedy Class II and III",
            "Kennedy Class I and IV",
            "Kennedy Class III and IV"
        ],
        "correct_answer": "Kennedy Class III and IV"
    },
    {
        "question": "A maxillary arch missing #4, 6, 7, 8,9,10 & 11 would be classified according to Kennedy Classification and Applegate's rules for classifying RPDs?",
        "options": [
            "Kennedy Class 3, no modification",
            "Applegate Class 4, modification 1",
            "Kennedy Class 3, modification 1",
            "Kennedy Class 4, modification 1",
            "None of the above"
        ],
        "correct_answer": "Kennedy Class 3, modification 1"
    },
    {
        "question": "When discussing Combination Syndrome and complete dentures, all of the following are true, except",
        "options": [
            "Occurs when an edentulous maxilla is opposed by a natural dentition and a mandibular Kennedy Class I RDP",
            "Extrusion/flaring of the mandibular anteriors and papillary hyperplasia are findings",
            "Mandibular bone loss beneath RDP distal extensions",
            "Absorption of maxillary tuberosities with accompanying loss of OVD",
            "Bone loss in maxillary anterior"
        ],
        "correct_answer": "Absorption of maxillary tuberosities with accompanying loss of OVD"
    },
    {
        "question": "Which of the following is true concerning rotational path RDP?",
        "options": [
            "With a category II rdp, seat rest associated with rigid connector 1st and rotate 2nd segment into place",
            "A category I rotational rdp can have lateral paths and is used to replace anterior teeth",
            "A category I rotational path rdp can be AP or PA but will replace posterior teeth",
            "There is only 1 category for a rotational path RDP."
        ],
        "correct_answer": "A category I rotational path rdp can be AP or PA but will replace posterior teeth"
    },
    {
        "question": "Advantages of rotational path RPD include all the following except",
        "options": [
            "Minimizes the number of clasps, reducing tooth coverage that may reduce plaque accumulation",
            "It can esthetically restore anterior gingival area with a flange",
            "May prevent further tipping of abutment teeth",
            "Can be used in absence of lingual or facial undercuts"
        ],
        "correct_answer": "It can esthetically restore anterior gingival area with a flange"
    },
    {
        "question": "Which of the following is/are false regarding lingualized occlusion and tooth selection?  1. According to Pound and Murrell, use 33o on the maxillary and 20o or 0o teeth teeth on the mandibular 2. When adjusting the mandibular posterior teeth remove the transverse ridges and even out the marginal ridges 3. The compensating curve begins with the first molars, with the distal cusps of the second molars 1.5 mm above the plane of the anteriors and bicuspids 4. All mandibular posteriors are set with 0o mediolateral curve",
        "options": [
            "(1) only",
            "(1) and (2) only",
            "(3) only",
            "(3) and (4)"
        ],
        "correct_answer": "(1) only"
    },
    {
        "question": "When treatment planning for a mandibular RDP lingual bar major connector, the height of the lingual vestibule must measure at least:",
        "options": [
            "9.0mm",
            "8.0mm",
            "6.0mm",
            "5.0mm"
        ],
        "correct_answer": "8.0mm"
    },
    {
        "question": "Which is not a requirement of a properly designed clasp assembly:",
        "options": [
            "Support - against vertical forces",
            "Encirclement - of more than half its abutment tooth circumference",
            "Elasticity - flex with equal and opposite forces as the occlusion forces",
            "Passivity - at rest when seated",
            "Retention - resist forces in a occlusal direction"
        ],
        "correct_answer": "Elasticity - flex with equal and opposite forces as the occlusion forces"
    },
    {
        "question": "In designing RDP's and using a surveyor, the following concepts need to be addressed and implemented EXCEPT?",
        "options": [
            "Start with the occlusal plane parallel to the deck (survey table)",
            "Adjust A-P tilt before lateral tilt to improve guide plane undercuts",
            "Height of contours are evaluated and marked with a graphite rod to determine adequate lateral tilt and where blockout might be needed",
            "Proper lateral tilt allows for slightly greater undercuts unilaterally to minimize tooth preparations"
        ],
        "correct_answer": "Proper lateral tilt allows for slightly greater undercuts unilaterally to minimize tooth preparations"
    },
    {
        "question": "Place the following stages of graft healing in order from earliest to latest.",
        "options": [
            "Organic Union, Plasmatic Circulation, Vascularization",
            "Plasmatic Circulation, Vascularization, Organic Union",
            "Vascularization, Organic Union, Plasmatic Circulation",
            "Vascularization, Plasmatic Circulation, Organic Union"
        ],
        "correct_answer": "Plasmatic Circulation, Vascularization, Organic Union"
    },
    {
        "question": "During the inItial stage (24-48HR) of connective tissue graft healing, the graft is nourished by diffusion from recipient bed through the fibrin clot, which is known as",
        "options": [
            "Vascularization",
            "Re-vascularization",
            "Plasma circulation",
            "Plasma diffusion"
        ],
        "correct_answer": "Plasma circulation"
    },
    {
        "question": "After the connective tissue graft begins to degenerate and necrose, where does the new epithelium proliferate from?",
        "options": [
            "The graft",
            "The recipient site",
            "Both the graft and the recipient site",
            "Neither the graft or the recipient site"
        ],
        "correct_answer": "The recipient site"
    },
    {
        "question": "Placement of membranes during GTR favors the repopulation of the area by which type of cells?",
        "options": [
            "Epithelium",
            "Periodontal ligament",
            "Fibrous tissue",
            "Blood cells"
        ],
        "correct_answer": "Periodontal ligament"
    },
    {
        "question": "What is false regarding primary or secondary occlusal trauma?  1. Primary occlusal trauma results from excessive occlusal force applied to a tooth or to teeth with unhealthy supporting tissues. 2. Secondary occlusal trauma refers to changes that occur when normal or abnormal occlusal forces are applied to the attachment apparatus of a tooth or teeth with adequate supporting tissues. 3. Primary occlusal trauma results from excessive occlusal force applied to a tooth or to teeth with normal and healthy supporting tissues. 4. Secondary occlusal trauma refers to changes that occur when normal or abnormal occlusal forces are applied to the attachment apparatus of a tooth or teeth with inadequate or reduced supporting tissues.",
        "options": [
            "(1) only",
            "(1) and (2)",
            "(2) only",
            "(3) and (4)"
        ],
        "correct_answer": "(1) and (2)"
    },
    {
        "question": "Which of the following bacteria is most commonly associated with pregnancy-associated gingivitis?",
        "options": [
            "B. forsythus",
            "P. gingivalis",
            "P. intermedia",
            "S. oralis"
        ],
        "correct_answer": "P. intermedia"
    },
    {
        "question": "The following periodontal fibers are most resistant to periodontitis?",
        "options": [
            "Transseptal",
            "Transgingival",
            "Intergingival",
            "Circular"
        ],
        "correct_answer": "Transseptal"
    },
    {
        "question": "Indications for osseous resective surgery include all of the following, except",
        "options": [
            "Shallow (1-2 mm) 2-walled (crater) intrabony defect",
            "3-walled intrabony defect",
            "1-walled (hemiseptum) defect normally located interproximally",
            "Reverse/negative bony architecture"
        ],
        "correct_answer": "3-walled intrabony defect"
    },
    {
        "question": "Advantages of laser treatment over the use of a scalpel include:",
        "options": [
            "Greater hemostasis",
            "Bactericidal effect",
            "Minimal wound contraction",
            "All the above"
        ],
        "correct_answer": "All the above"
    },
    {
        "question": "Which of the following periodontal term is defined as the healing in the area of the root not previously exposed to the pocket after surgical detachment of the tissues or following traumatic tears in the cementum, tooth fractures, or the treatment of periapical lesions?",
        "options": [
            "Regeneration",
            "Reattachment",
            "New Attachment",
            "Repair"
        ],
        "correct_answer": "Reattachment"
    },
    {
        "question": "Smokers are more susceptible to periodontal disease due to",
        "options": [
            "Lower levels of bacterial pathogens such as B forsythus or P gingivalis in subgingival sites",
            "Impaired function of host response in neutralizing infection and overstimulation of host response to destroy surrounding tissue",
            "Generally having more periodontal pathogens presents at 70-85% more sites than nonsmokers.",
            "Increased amounts of salivary antibodies (immunoglobulin A, or IgA,) and serum IgG antibody response to Prevotella intermedia and Fusobacterium nucleatum"
        ],
        "correct_answer": "Impaired function of host response in neutralizing infection and overstimulation of host response to destroy surrounding tissue"
    },
    {
        "question": "All of the following are rules that should be followed when placing intracrevicular margins EXCEPT:",
        "options": [
            "If the sulcus probes 1.5mm or less, place the restoration margin 0.5mm below the gingival tissue crest.",
            "If the sulcus probes more than 1.5mm, place the margin one half the depth of the sulcus below the tissue crest.",
            "If a sulcus greater than 2mm is found, evaluate to see if a gingivectomy could be performed to create a 1.5mm sulcus.",
            "All the above are correct."
        ],
        "correct_answer": "All the above are correct."
    },
    {
        "question": "Which one of the following does not tend to occur when the biologic width is violated by a restoration",
        "options": [
            "Chronic pain",
            "Chronic inflammation",
            "Unpredictable loss of alveolar bone",
            "Enhance crown to root ratio"
        ],
        "correct_answer": "Enhance crown to root ratio"
    },
    {
        "question": "Which of the following is false relative to biological width, and the dentogingival complex?",
        "options": [
            "The biologic width is defined as the dimension of the soft tissue, which is attached to the portion of the tooth coronal to the crest of the alveolar bone.",
            "Regarding overhangs on restorations, the severity of bone loss is directly proportional to the severity of the overhang.",
            "Crown lengthening may be accomplished by surgery, by orthodontic forced eruption, or a combination of both.",
            "Gargiulo et al. (1961) reported the following mean dimensions: a sulcus depth of 0.97mm, an epithelial attachment of 0.69mm, and a connective tissue attachment of 1.07mm."
        ],
        "correct_answer": "Gargiulo et al. (1961) reported the following mean dimensions: a sulcus depth of 0.97mm, an epithelial attachment of 0.69mm, and a connective tissue attachment of 1.07mm."
    },
    {
        "question": "Which of the following most accurately describes how epithelium that is sloughed and lost during a connective tissue graft is replaced by new epithelial growth?",
        "options": [
            "While undergoing epithelial necrosis, molecular communicative factors from tissue debris stimulate new growth.",
            "Locally accumulated macrophages release growth factors upon phagocytosis that initiate new epithelial regeneration in a process known in histological research communities as squamous poop eating.",
            "Chemotactic initiators from local vasculature induce epithelial growth by diffusion and hydration.",
            "Genetic predetermination of the oral mucosa that is dependent on stimuli that originate in the connective tissue."
        ],
        "correct_answer": "Genetic predetermination of the oral mucosa that is dependent on stimuli that originate in the connective tissue."
    },
    {
        "question": "When considering endodontic-periodontic lesions, all of the following are true except?",
        "options": [
            "A true combined lesion may mimic (in appearance) a vertical root fracture radiographically",
            "Pulp and the periodontal ligament communicate via dentinal tubules, lateral/accessory canals and furcal canals",
            "In addressing a primary endodontic lesion with a secondary periodontal lesion, periodontal treatment is performed first followed by NSRCT",
            "In a primary periodontal defect with secondary endodontic involvement, expect probing depths wider coronally then apically as well as the perio disease infecting the pulp through lateral and accessory canals"
        ],
        "correct_answer": "In addressing a primary endodontic lesion with a secondary periodontal lesion, periodontal treatment is performed first followed by NSRCT"
    },
    {
        "question": "Which of the following are true concerning antibiotics used for periodontal disease:",
        "options": [
            "Atridox® is effective because its active ingredient is chlorhexidine",
            "Arestin is effective because it is a locally delivered, substained-release form of minocycline microspheres",
            "Actisite® is effective because its active ingredient is metronidazole",
            "Periochip® is effective because its active ingredient, tetracycline, is released slowly over a two week period"
        ],
        "correct_answer": "Arestin is effective because it is a locally delivered, substained-release form of minocycline microspheres"
    },
    {
        "question": "Which of the following local delivering devices does not contain any tetracycline or tetracycline derivative?",
        "options": [
            "Arestin",
            "Atridox",
            "Periochip",
            "Periostat"
        ],
        "correct_answer": "Periochip"
    },
    {
        "question": "The FDA approved and ADA accepted antimicrobial agent, Atridox, is",
        "options": [
            "Locally delivered with 10% doxycycline gel using a syringe",
            "Locally delivered with 10% doxycycline microspheres using a syringe",
            "Locally delivered with 30% doxycycline gel using a syringe",
            "Systemically and locally delivered with 10% doxycycline tablet"
        ],
        "correct_answer": "Locally delivered with 10% doxycycline gel using a syringe"
    },
    {
        "question": "Once Actisite tetracycline fiber is packed into a periodontal pocket a sustained dosage of 1300 μg/ml is sustained, well beyond the 32-64μg/ml required to inhibit the growth of pathogens. In contrast, crevicular fluid concentraions of 2000 to 2200μg/ml are reported after systemic administration of tetracycline of 250mg qid.",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "The first statement is true and the second is false",
            "The first statement is false and the second is true"
        ],
        "correct_answer": "The first statement is true and the second is false"
    },
    {
        "question": "Chlorohexidine has an immediate bacteriocidal effect but has a prolonged bacteriostatic effect and inhibits the formation of plaque by what mechanism?",
        "options": [
            "Positive charge",
            "Adsorption to pellicle",
            "Adsorption to cementum",
            "Sticky consistency"
        ],
        "correct_answer": "Adsorption to pellicle"
    },
    {
        "question": "Which of the following is false regarding Triclosan?",
        "options": [
            "It is regarded as an antibacterial agent in the Pharmacologic Category",
            "It is used in the prevention of dental caries and gingivitis",
            "To provide a longer retention time of the tricloscan in plaque, a polymer has been added to the toothpaste vehicle",
            "There is no generic form available"
        ],
        "correct_answer": "It is used in the prevention of dental caries and gingivitis"
    },
    {
        "question": "The prevalence of cervical enamel projections are highest for which of the following teeth?",
        "options": [
            "Mandibular and maxillary second molars",
            "Mandibular and maxillary first molars",
            "Mandibular first molars and maxillary second molars",
            "Mandibular second and maxillary first molars"
        ],
        "correct_answer": "Mandibular and maxillary second molars"
    },
    {
        "question": "F. All of the above F. All of the above When discussing the bacteria associated with periodontal diseases, all of the following associations are true, except",
        "options": [
            "Pregnancy gingivitis is associated with high levels of Prevotella intermedia (Pi)",
            "As chronic periodontitis progresses, the plaque microflora becomes more anaerobic, Gram -, motile, and inflammatory consequences intensify",
            "Aggressive periodontitis has a strong association with Aa",
            "The red complex (most pathogenic) in relation to chronic periodontitis, includes Porphyromona gingivalis, Treponema denticola and Fusobacterium nucleatum"
        ],
        "correct_answer": "The red complex (most pathogenic) in relation to chronic periodontitis, includes Porphyromona gingivalis, Treponema denticola and Fusobacterium nucleatum"
    },
    {
        "question": "List, in order, the steps to perform the Modified Widman flap technique:  1. Incision is an internal bevel incision to the alveolar crest starting 0.5 to 1mm away from the gingival margin. 2. The gingival is reflected, leaving a wedge of tissue of tissue still attached by its base. 3. A crevicular incision is made from the bottom of the pocket to the bone. 4. An incision is made in the interdental spaces coronal to the bone with a curette. Tissue tags and granulation tissue are moved with a curette. Root surfaces are scaled and planed. 5. The flaps may be thinned to allow for close adaptation of the gingival around the entire circumference of the tooth and replaced in its original position.",
        "options": [
            "3, 1, 2, 4, 5",
            "1, 2, 3, 4, 5",
            "3, 4, 1, 2, 5",
            "1, 2, 5, 3, 4"
        ],
        "correct_answer": "1, 2, 3, 4, 5"
    },
    {
        "question": "Which of the following statements about papilla preservation flaps is false?",
        "options": [
            "The papilla preservation flap should be used for narrow interdental spaces.",
            "A crevicular incision around each tooth is made with no incisions across the interdental papilla.",
            "The Orban knife is used to sever 1/2 to 2/3 of the base of the interdental papilla.",
            "The flap is reflected without thinning the tissue."
        ],
        "correct_answer": "The papilla preservation flap should be used for narrow interdental spaces."
    },
    {
        "question": "Vertical releasing incisions are indicated in all the following, except",
        "options": [
            "Extending beyond the mucogingival line, reaching the alveolar mucosa",
            "At the line angles of the tooth and should include the entire papilla or none at all",
            "Designed to avoid short flap (mesial distally) that is long apical-gingival flap",
            "At both ends if the flap is apically displaced."
        ],
        "correct_answer": "Designed to avoid short flap (mesial distally) that is long apical-gingival flap"
    },
    {
        "question": "The following are indications to extrude a tooth except?",
        "options": [
            "To gain adequate biologic width",
            "To level the free gingival margin of teeth",
            "To reduce a vertical bony defect",
            "To prepare a site for an immediate implant",
            "All of the above are indications for extrusion"
        ],
        "correct_answer": "All of the above are indications for extrusion"
    },
    {
        "question": "When used in GBR/GTR BMP's stimulate the differentiation of what type of cells to form chondroblasts and osteoblasts?",
        "options": [
            "Mesenchymal cells",
            "Endocrine cells",
            "Endothelial cells",
            "Endoderm",
            "Ectoderm"
        ],
        "correct_answer": "Mesenchymal cells"
    },
    {
        "question": "Which of the following has been used to induce root surface biocompatibility and enhance cellular response?",
        "options": [
            "Fibronectin",
            "Laminin",
            "Tetracycline",
            "A and C only",
            "All of the above"
        ],
        "correct_answer": "All of the above"
    },
    {
        "question": "Which of the following factors is believed to most significantly influence the development of plaque-induced gingivitis?",
        "options": [
            "Elevated hormone levels",
            "Poor oral hygiene",
            "Cardiovascular disease",
            "Low socioeconomic status"
        ],
        "correct_answer": "Poor oral hygiene"
    },
    {
        "question": "What perio exam criteria identify a tooth as hopeless?",
        "options": [
            "Tooth mobility with slight bone loss",
            "Tooth mobility with advanced bone loss",
            "Grade II furcation involvement",
            "Grade III furcation involvement only"
        ],
        "correct_answer": "Tooth mobility with advanced bone loss"
    },
    {
        "question": "Tarnow related the presence or absence of the papilla between two teeth is determined by the distance from the crest of bone to the contact point. Which of the following statement is incorrect?",
        "options": [
            "When the distance was 5 mm or less, the papilla completely filled this space approximately 100% of the time.",
            "A small difference of 1 mm was clinically significant.",
            "When the distance was 6 mm, the interdental space filled about 55% of the time.",
            "When an implant is placed adjacent to a tooth, a greater than 5 mm distance between the contact point and the crest of the bone is recommended for the papilla to completely fill this space."
        ],
        "correct_answer": "When an implant is placed adjacent to a tooth, a greater than 5 mm distance between the contact point and the crest of the bone is recommended for the papilla to completely fill this space."
    },
    {
        "question": "Cross-cut fissured burs are designed to do all the following except",
        "options": [
            "Increase cutting efficiency",
            "Plane the tooth surface",
            "Cutting dentin and enamel",
            "Remove old restorations"
        ],
        "correct_answer": "Plane the tooth surface"
    },
    {
        "question": "The metal component of an admixed amalgam is produced by:",
        "options": [
            "Lathe cutting an ingot of alloy",
            "The alloy is melted and then sprayed under high pressure",
            "Both A and B",
            "Neither A or B"
        ],
        "correct_answer": "Both A and B"
    },
    {
        "question": "Condensing amalgam with a larger diameter nib as compared to a small diameter nib requires?",
        "options": [
            "More condensation force",
            "Less condensation force",
            "Same condensation force"
        ],
        "correct_answer": "More condensation force"
    },
    {
        "question": "Excessive trituration should be avoided because:  1. It generates heat and creates an inadequate matrix in the microstructure of the resulting set material 2. It will set prematurely after trituration 3. It prevents adequate condensation and adaptation to the walls of the preparation, 4. It will result in a weakened restoration.",
        "options": [
            "(1) and (3)",
            "(1) and (4)",
            "(2), (3), and (4)",
            "All of the above"
        ],
        "correct_answer": "(2), (3), and (4)"
    },
    {
        "question": "Which of the following is not correct regarding the mercury content of amalgam restorations?",
        "options": [
            "Restorations containing increasing quantities of mercury exhibit decreasing strength values.",
            "Higher concentrations of mercury are located around the margins of the restoration.",
            "The compressive strength decreases 1% for each 1% increase in mercury above 60%.",
            "Uniform concentrations of mercury are typically present throughout well-condensed restorations."
        ],
        "correct_answer": "Uniform concentrations of mercury are typically present throughout well-condensed restorations."
    },
    {
        "question": "Glass ionomers consist of an ion-leachable aluminosilicate glass powder and a phosphoric acid liquid. Carboxylic acid groups (-COOH) chemically bond to calcium on exposed tooth surface.",
        "options": [
            "Both statements are true.",
            "Both statements are false.",
            "The first statement is true and the second statement is false.",
            "The first statement is false and the second statement is true."
        ],
        "correct_answer": "The first statement is false and the second statement is true."
    },
    {
        "question": "Which one of the following statements is true?",
        "options": [
            "A compomer is a composite to which some glass-ionomer components have been added.",
            "Compomers have better physical characteristics than composites.",
            "Compomers are capable of releasing fluoride at a constant rate.",
            "Compomers have low wear resistance and low strength when compared to conventional glass ionomer."
        ],
        "correct_answer": "A compomer is a composite to which some glass-ionomer components have been added."
    },
    {
        "question": "What is the correct order of the compressive strengths from lowest to highest?",
        "options": [
            "Resin Modified Glass Ionomer, Glass Ionomer, Nanocomposite, Compomer",
            "Compomer, Nanocomposite, Glass Ionomer, Resin Modified Glass Ionomer",
            "Glass Ionomer, Resin Modified Glass Ionomer, Compomer, Nanocomposite",
            "Nanocomposite, Compomer, Resin Modified Glass Ionomer, Glass Ionomer"
        ],
        "correct_answer": "Glass Ionomer, Resin Modified Glass Ionomer, Compomer, Nanocomposite"
    },
    {
        "question": "When considering physical properties, hybrid glass ionomers (RMGI) compared to glass ionomers have",
        "options": [
            "Slightly lower fluoride release/rechargability, higher compressive strength, and better esthetics",
            "Equal fluoride release/rechargability, higher compressive strength, and better esthetics",
            "Slightly higher fluoride release/rechargability, higher compressive strength, better esthetics",
            "Slightly lower fluoride release, lower compressive strength, and better esthetics"
        ],
        "correct_answer": "Slightly lower fluoride release/rechargability, higher compressive strength, and better esthetics"
    },
    {
        "question": "In office bleaching is usually above what percentage of Hydrogen peroxide?",
        "options": [
            "5%",
            "15%",
            "25%",
            "35%"
        ],
        "correct_answer": "35%"
    },
    {
        "question": "Whereas normal bleaching time is 2 to 6 weeks some tetracycline stained teeth may require 2-12months of daily treatment. Teeth stained in what section have the poorest prognosis?",
        "options": [
            "Incisal third",
            "Middle third",
            "Gingival third"
        ],
        "correct_answer": "Gingival third"
    },
    {
        "question": "Self-etch systems contain mild (pH + 2), intermediary strong (pH + 1.5), and strong (pH <1) adhesive classes. The micromorphologic aspect of strong self-etch adhesives is very similar to that of etch-and-rinse adhesives and is characterized by a 3- to 5- um thick hybrid layer and extensive resin tags.",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "The first statement is true, the second statement is false",
            "The first statement is false, the second statement is true"
        ],
        "correct_answer": "Both statements are true"
    },
    {
        "question": "Which statement is true when comparing bond strengths of self-etching adhesive systems on prepared versus unprepared enamel?",
        "options": [
            "A higher microtensile bond strength is expected when bonding to prepared enamel versus unprepared enamel.",
            "A lower microtensile bond strength is expected when bonding to prepared enamel versus unprepared enamel.",
            "While a difference in microtensile bond strength is exists, no statistically significant difference is evident.",
            "No difference in microtensile bond strength exists between prepared and unprepared enamel."
        ],
        "correct_answer": "A higher microtensile bond strength is expected when bonding to prepared enamel versus unprepared enamel."
    },
    {
        "question": "What is the design for performing a mini-flap when restoring root surface caries?",
        "options": [
            "Incisions at the mesial and distal line angles straight apically",
            "Incisions at the line angles, initially toward the papilla and then apically",
            "Vertical incisions that bisect the papilla on each side",
            "Envelope flap incorporating at least 1 tooth on either side"
        ],
        "correct_answer": "Incisions at the line angles, initially toward the papilla and then apically"
    },
    {
        "question": "All of the following are considerations when preparing tetracycline stained teeth for veneers EXCEPT?",
        "options": [
            "Ensure proximal extensions are into the contact area",
            "Vital bleaching should be an adjunct before veneer preparations are made",
            "Color modifiers (unfilled resins) are useful in covering tetracycline staining",
            "Ensure all discolored enamel is removed down to expose dentin"
        ],
        "correct_answer": "Ensure all discolored enamel is removed down to expose dentin"
    },
    {
        "question": "Steps in preparing a veneer for diastema closure include all the following except:",
        "options": [
            "The window preparation typically is made with a facial surface reduction of 0.5 to 0.75 mm midfacially",
            "The gingival margin is reduced to a depth of 0.2 to 0.5mm",
            "The preparation is terminated just facial to the proximal contact area",
            "The incisal edge is preserved to protect the veneer from heavy functional forcess"
        ],
        "correct_answer": "The preparation is terminated just facial to the proximal contact area"
    },
    {
        "question": "Which of the following statements concerning the effects of light and heat on the bleaching process is correct?",
        "options": [
            "Light speeds the bleaching reaction. Heat speeds the bleaching reaction.",
            "Light speeds the bleaching reaction. Heat slows the bleaching reaction.",
            "Light slows the bleaching reaction. Heat speeds the bleaching reaction.",
            "Light slows the bleaching reaction. Heat slows the bleaching reaction."
        ],
        "correct_answer": "Light speeds the bleaching reaction. Heat speeds the bleaching reaction."
    },
    {
        "question": "Which statement comparing QTH and LED light curing units is correct?",
        "options": [
            "QTH means Quartz-Tungsten Halogen light and LED means Light Emitting Dioxide",
            "Both QTH and LED unit have peak wavelengths varying from 450-490 nm.",
            "Both QTH and LED require a filter, reflector and a fan to reduce the heat output",
            "Only QTH can cure material with camphorquinone photo-initiator more efficiently compared to LED"
        ],
        "correct_answer": "Both QTH and LED unit have peak wavelengths varying from 450-490 nm."
    },
    {
        "question": "Which of the following types of curing lights produces the narrowest spectrum of light without being filtered?",
        "options": [
            "QTH",
            "PAC",
            "LED",
            "LMNOP"
        ],
        "correct_answer": "LED"
    },
    {
        "question": "What type of margin is preferred when preparing a veneer?",
        "options": [
            "Shoulder",
            "Chamfer",
            "Feather edge",
            "Chisel edge"
        ],
        "correct_answer": "Chamfer"
    },
    {
        "question": "Regarding taper of a crown prep:  When prep height and diameter are equal, the prep with the greater taper will have a decrease in resistance. The taper that provides resistance for a prep where the height is equal to the base is 2X that of that prep where height equals ½ the base",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "The first statement is true, the second is false",
            "The first statement is false, the second is true"
        ],
        "correct_answer": "Both statements are true"
    },
    {
        "question": "The flexural and compressive moduli of microfilled and flowable composites are about 50% lower than values for the multipurpose hybrids and packable composite resin restorations. This reflects the lower volume percent of filler present in microfilled and flowable composites.",
        "options": [
            "The first statement is true, the second statement is false.",
            "The first statement is false, the second statement is true.",
            "Both statements are true.",
            "Both statements are false."
        ],
        "correct_answer": "Both statements are true."
    },
    {
        "question": "The differences between a packable composite and a hybrid one are:  a) the inorganic filler material of hybrid composites is approximately 80 % by weight b) packable composites are less viscous than hybrid composites c) the hybrid composites inorganic fillers have an average particle size of 0.4 to 1 m d) the packables have a smoother surface texture in the finished restoration e) a and c e) a and c When considering coefficient of thermal expansion (COTE), which material has the highest COTE on average?",
        "options": [
            "Pit and fissure sealants",
            "Composite resins",
            "Amalgam",
            "Gold",
            "Glass Ionomer"
        ],
        "correct_answer": "Pit and fissure sealants"
    },
    {
        "question": "Which of the following statements is true regarding adhesive of resins to dentin?",
        "options": [
            "The 3-step total etch system includes: etchant, primer, and bonding agent.",
            "The all-in-one self-etch technique etches the enamel and removes the smear layer.",
            "The bonding agent in a total etch system includes monomers that are mostly hydrophilic such as Bis-GMA.",
            "All in one self etching adhesive are hydrophobic and not likely to undergo water degradation."
        ],
        "correct_answer": "The 3-step total etch system includes: etchant, primer, and bonding agent."
    },
    {
        "question": "Arrange the order of these adhesives according to their bond strengths from lowest to highest.",
        "options": [
            "Total-etch two-step; Self-etch one-step; Self-etch two-step",
            "Total-etch two-step; Self-etch two-step; Self-etch one-step",
            "Self-etch two-step; Self-etch one-step; Total-etch two-step",
            "Self-etch one-step; Self-etch two-step; Total-etch two-step"
        ],
        "correct_answer": "Self-etch one-step; Self-etch two-step; Total-etch two-step"
    },
    {
        "question": "Which statement regarding packable resins and hybrid composite is correct?",
        "options": [
            "Packable resins have superior marginal integrity",
            "Hybrid resins are more resistant to surface texture loss over time",
            "Hybrid resins have noticeably better color match",
            "Both systems have similar color match and marginal discoloration"
        ],
        "correct_answer": "Both systems have similar color match and marginal discoloration"
    },
    {
        "question": "TEGDMA (triethylene glycol dimethacrylate) serves what function in composite?",
        "options": [
            "Photoinitiator",
            "Viscosity reduction",
            "Color stabilizer",
            "Filler"
        ],
        "correct_answer": "Viscosity reduction"
    },
    {
        "question": "Transillumination may be most helpful in detecting caries in what location of the mouth?",
        "options": [
            "Posterior teeth",
            "Anterior proximal caries",
            "Class V lesions",
            "Pits and fissures"
        ],
        "correct_answer": "Anterior proximal caries"
    },
    {
        "question": "In amalgam bonding, the mechanism for attachment of the bonding resin to tooth structure is identical to the mechanism that resin bonding systems use to attach resin composite to dentin and enamel. However, the amalgam-to-resin attachment is entirely mechanical.",
        "options": [
            "The first statement is true, the second statement is false.",
            "The first statement is false, the second statement is true.",
            "Both statements are true.",
            "Both statements are false."
        ],
        "correct_answer": "Both statements are true."
    },
    {
        "question": "The use of amalgam bonding has several possible benefits except:",
        "options": [
            "Less need for the removal of tooth structure such as grooves and dovetails",
            "Bonded amalgam may increase the fracture resistance of restored teeth",
            "The adhesive resin liner may seal margins better than the traditional cavity varnishes with decreased risks for postoperative sensitivity",
            "Long-term clinical and laboratory studies are well established for its effectiveness"
        ],
        "correct_answer": "Long-term clinical and laboratory studies are well established for its effectiveness"
    },
    {
        "question": "When considering placing a fiber post following NSRCT, all of the following are true, EXCEPT",
        "options": [
            "The post length should be at least ½ the length of the root contained in the remaining radiographic bone",
            "One should prepare the canal for the largest fiber post thus maximizing retention of the core",
            "The purpose of the post is not to reinforce endodontically treated teeth but is to retain the core",
            "The best retention for a fiber post will most likely be achieved using etch and rinse and self cure resin cement"
        ],
        "correct_answer": "One should prepare the canal for the largest fiber post thus maximizing retention of the core"
    },
    {
        "question": "Which of the following statement is incorrect concerning the use of a non-rigid fiber post?",
        "options": [
            "Bonding fiber posts to root canal dentin can improve the distribution of forces applied along the root",
            "A cemented fiber post is retentive with the least amount of stress generated on the canal walls",
            "Most failures of fiber posts are due to catastrophic root fractures",
            "A light transmitting post results in better polymerization of resin composites in the apical area of a root canal"
        ],
        "correct_answer": "Most failures of fiber posts are due to catastrophic root fractures"
    },
    {
        "question": "Which of the following shows the correct order of luting a porcelain veneer with a resin cement after removal of provisionals.",
        "options": [
            "Try-in paste; Rinse thoroughly, Etch veneer with 35% phosphoric acid, Primer in veneer, Single bond adhesive in veneer, Etch tooth with 35% phosphoric acid, Single bond adhesive, Resin Cement in Veneer.",
            "Try-in paste, Rinse thoroughly, Etch tooth with 35% phosphoric acid, Single bond adhesive, Resin Cement in Veneer",
            "Try-in paste, Rinse thoroughly, Etch veneer with 35% phosphoric acid, Primer in veneer, Single bond adhesive in veneer, Etch tooth with 35% phosphoric acid, Single bond adhesive, Resin Cement in Veneer Rinse thoroughly, Etch tooth with 35% phosphoric acid, Single bond adhesive, Resin Cement placed on tooth.",
            "Try-in paste, Rinse thoroughly, Etch veneer with 35% phosphoric acid, Primer in on tooth, Single bond adhesive in veneer, Etch tooth with 35% phosphoric acid, Single bond adhesive, Resin Cement in Veneer"
        ],
        "correct_answer": "Try-in paste; Rinse thoroughly, Etch veneer with 35% phosphoric acid, Primer in veneer, Single bond adhesive in veneer, Etch tooth with 35% phosphoric acid, Single bond adhesive, Resin Cement in Veneer."
    },
    {
        "question": "Compared to hybrid composite, compomers have all the following characteristics, EXCEPT",
        "options": [
            "Compomers contain poly-acid modified monomers with fluoride releasing silicate glasses",
            "Setting occurs primarily by light-cured polymerization, but acid-base reaction also occur as compomers absorb water upon contact with saliva",
            "Compomers have higher compressive strength and can have fluoride recharged from daily fluoride exposure",
            "Both materials can be used to restore Class 1 and 2 in primary teeth"
        ],
        "correct_answer": "Compomers have higher compressive strength and can have fluoride recharged from daily fluoride exposure"
    },
    {
        "question": "Which of the following is not an advantage to using composite as a core material?",
        "options": [
            "Adequate compressive strength",
            "Adequate fracture toughness",
            "Dimensional stability in a wet environment",
            "Tooth colored material for use under all ceramic restorations"
        ],
        "correct_answer": "Dimensional stability in a wet environment"
    },
    {
        "question": "Retention grooves placed on the mesial and distal of a crown prep increase the resistance to dislodgement of forces in which direction?",
        "options": [
            "Buccal lingual",
            "Mesial distal",
            "Occluso vertical"
        ],
        "correct_answer": "Buccal lingual"
    },
    {
        "question": "The advantage of the ultrathin metal matrices (\"ring\") system for the placement of posterior Class II composites are all of the following except:",
        "options": [
            "Tight interproximal contacts are more easily developed",
            "They provide better proximal contours",
            "They simplify matrix placement for single proximal-surface restorations",
            "Used with the plastic, light-reflecting wedge creates a more effective interproximal contact"
        ],
        "correct_answer": "Used with the plastic, light-reflecting wedge creates a more effective interproximal contact"
    },
    {
        "question": "Which of the following represents the correct order of increasing flexural strength of various dental ceramics?",
        "options": [
            "Feldspar, lithium disilicate, leucite, zirconia, alumina",
            "Feldspar, leucite, lithium disilicate, alumina, zirconia",
            "Leucite, feldspar, alumina, lithium disilicate, zirconia",
            "Feldspar, zirconia, alumina, leucite, lithium disilicate"
        ],
        "correct_answer": "Feldspar, leucite, lithium disilicate, alumina, zirconia"
    },
    {
        "question": "Which type of porcelain is resistant to etching with hydrofluoric acid?",
        "options": [
            "Stackable porcelains",
            "In-ceram porcelains",
            "Pressable porcelains",
            "Stripped porcelains"
        ],
        "correct_answer": "In-ceram porcelains"
    },
    {
        "question": "When considering properties of porcelain, all of the following are true EXCEPT?",
        "options": [
            "1st generation pressable ceramics are reinforced with leucite crystals and stronger than feldspathic porcelains",
            "2nd generation pressable ceramics are reinforced with lithium disilicate crystals",
            "CEREC (machined leucite) restorations have a higher flexural strength (MPa) than E-max restorations",
            "Hardness does not correlate to wear opposing dentition"
        ],
        "correct_answer": "CEREC (machined leucite) restorations have a higher flexural strength (MPa) than E-max restorations"
    },
    {
        "question": "Dicor ceramic restoration is fabricated by using which of the following methods?",
        "options": [
            "Pressure molded under heat using lost wax technique",
            "Cast from a melted ceramic ingot",
            "Milled using CAD/CAM",
            "Glass infused alumina or zirconia core with stacked body porcelain",
            "Lithium disilicate core with glass-ceramic veneer"
        ],
        "correct_answer": "Cast from a melted ceramic ingot"
    },
    {
        "question": "Arrange these machined dental ceramics according to flexural strengths from lowest to highest.",
        "options": [
            "Zirconia, alumina, feldspathic, leucite",
            "Feldspathic, leucite, alumina, zirconia",
            "Leucite, zirconia, feldspathic, alumina,",
            "Alumina, leucite, zirconia, feldspathic"
        ],
        "correct_answer": "Feldspathic, leucite, alumina, zirconia"
    },
    {
        "question": "The primary function of leucite added to dental ceramics is",
        "options": [
            "To raise the coefficient of thermal expansion, consequently increasing the hardness and fusion temperatures",
            "To increase opacity for better esthetic restorations and custom color match",
            "To decrease the coefficient of thermal expansion, consequently increase the hardness and fusion temperatures.",
            "To decrease phase transformation toughness to prevent the propagation of surface cracks"
        ],
        "correct_answer": "To raise the coefficient of thermal expansion, consequently increasing the hardness and fusion temperatures"
    },
    {
        "question": "Place the following porcelains in order from greatest to the least amount of translucency.",
        "options": [
            "Zirconium, lithium disilicate, feldspathic, leucite.",
            "Feldspathic, leucite, lithium disilicate, zirconium",
            "Leucite, feldspathic, lithium disilicate, zirconium",
            "Feldspathic, lithium disilicate, leucite, zirconium"
        ],
        "correct_answer": "Feldspathic, leucite, lithium disilicate, zirconium"
    },
    {
        "question": "What is the most abundant mineral in most high-medium-and low fusing porcelains?",
        "options": [
            "SiO2 - quartz",
            "Al2O3 - Aluminum oxide",
            "Na2O - Sodium Oxide",
            "K2O- Potassium oxide"
        ],
        "correct_answer": "SiO2 - quartz"
    },
    {
        "question": "Self-glazing, the traditional final step in the fabrication of MCR crowns, does not significantly improve the flexural strength of feldspathic dental ceramics. Application of a low-expansion glass called glaze to the surface of a ceramic which is then fired to a high temperature is known to reduce depth and width of the surface flaws, thereby improving the overall resistance of the ceramic to crack propagation.",
        "options": [
            "The first statement is true, the second statement is false.",
            "The first statement is false, the second statement is true.",
            "Both statements are true.",
            "Both statements are false."
        ],
        "correct_answer": "Both statements are true."
    },
    {
        "question": "Which statement is true when identifying the strongest, pressable wear characteristics of porcelain?",
        "options": [
            "The CTE of porcelain must be less than metal for retention of porcelain to a metal substructure",
            "Compression of the porcelain on a PFM is a main factor in porcelain retention to the metal substructure.",
            "Highly esthetic dental ceramics are predominantly glassy, and higher strength substructure ceramics are generally crystalline.",
            "All are true"
        ],
        "correct_answer": "All are true"
    },
    {
        "question": "When considering low fusing porcelains, all of the following are true, EXCEPT",
        "options": [
            "Low fusing porcelains can have an opaque, dentin, enamel, translucent, and body modifier layers when used with MCR restorations",
            "Low fusing porcelains have minimal or no leucite content thus decreasing wear on opposing dentition",
            "Grain size and porosity of low fusing porcelains dictate amount of wear",
            "Feldspathic veneering porcelain has a high flexural strength (100-150 MPa)"
        ],
        "correct_answer": "Feldspathic veneering porcelain has a high flexural strength (100-150 MPa)"
    },
    {
        "question": "Overglazing porcelain will result in which of the following?",
        "options": [
            "Porcelain will fracture",
            "Porcelain will become milky or cloudy in appearance",
            "Porcelain will turn green",
            "Will result in porosity on the surface"
        ],
        "correct_answer": "Porcelain will become milky or cloudy in appearance"
    },
    {
        "question": "One can polish dental ceramics with",
        "options": [
            "Overglaze and Natural Glaze",
            "Green Stone, White Stone, Diamond Paste",
            "Overglaze, Natural Glaze, Green Stone, White Stone, Diamond Paste",
            "Sof-Lex discs, Overglaze, Natural Glaze, Green Stone, White Stone, Diamond Paste"
        ],
        "correct_answer": "Sof-Lex discs, Overglaze, Natural Glaze, Green Stone, White Stone, Diamond Paste"
    },
    {
        "question": "The following are steps for bonding of zirconia based ceramics with resin cement is true, except?",
        "options": [
            "Tribochemical silica coating (Rocatec Soft/3M)",
            "Prime and bond for light-cured resin cements with a silaning agent",
            "A silane coupling agent is applied to achieve chemical bonding to the silica-coated surface",
            "Air-particle abrasion with alumina oxide particles"
        ],
        "correct_answer": "Prime and bond for light-cured resin cements with a silaning agent"
    },
    {
        "question": "Which of the following is the least likely cause of ceramic inlay failure?",
        "options": [
            "Debonding of the restoration",
            "Bulk fracture",
            "Marginal breakdown",
            "All the above are equal causes of ceramic inlay failures"
        ],
        "correct_answer": "Debonding of the restoration"
    },
    {
        "question": "When a segment of a veneer fractures but remains intact, it is defined as what type of fracture?",
        "options": [
            "Cohesive",
            "Static",
            "Adhesive",
            "Marginal"
        ],
        "correct_answer": "Static"
    },
    {
        "question": "Which of the following techniques should be incorporated in the medical model of caries management?",
        "options": [
            "Eliminate susceptible areas by sealing pits and fissures",
            "Reduce oral flora with chlorhexidine treatment",
            "Recommend diet modification by reducing the source of carbohydrate intake",
            "Induce remineralization with daily, low-dose fluoride application",
            "All of the above"
        ],
        "correct_answer": "All of the above"
    },
    {
        "question": "Recommendations in an all ceramic inlay/onlay preparation include all of the following except:",
        "options": [
            "Margins should not fall on centric contact points",
            "Areas to be onlayed need 1.5mm of clearance in all excursions",
            "Bevels are contraindicated",
            "The central groove reduction (2.5mm) follows the anatomy of the unprepared tooth"
        ],
        "correct_answer": "The central groove reduction (2.5mm) follows the anatomy of the unprepared tooth"
    },
    {
        "question": "How do ceramic inlays/onlays most commonly fail?",
        "options": [
            "Fracture and debonding",
            "Debonding due to method of cementation",
            "Debonding and marginal breakdown",
            "Fracture and marginal breakdown"
        ],
        "correct_answer": "Fracture and marginal breakdown"
    },
    {
        "question": "Which of the following impression material is most accurate in a wet environment?",
        "options": [
            "Condensation silicones",
            "Polysuflides",
            "Polyethers",
            "Addition silicones"
        ],
        "correct_answer": "Polyethers"
    },
    {
        "question": "Which of the following statements concerning dentin desensitizers is false?",
        "options": [
            "Arginine and Calcium Carbonate seals the dentin tubules to stop sensitivity.",
            "Using 5% potassium nitrate toothpaste will depolarize the nerves and stop neural transmission.",
            "Potassium nitrates occlude the dentinal tubules to stop sensitivity.",
            "Arginine and Calcium Carbonates will depolarize the nerves and stop neural transmission."
        ],
        "correct_answer": "Potassium nitrates occlude the dentinal tubules to stop sensitivity."
    },
    {
        "question": "Which desensitizing agents and proposed mechanism of action is incorrect?",
        "options": [
            "Potassium nitrate -reduce nerve excitability in animal models.",
            "Oxalates - reduce dentin permeability and occlude tubules",
            "Calcium phosphates-remineralize the enamel crystalline structure",
            "Fluoride -reduce dentin sensitivity possibly by precipitation of insoluble calcium fluoride within the tubules."
        ],
        "correct_answer": "Calcium phosphates-remineralize the enamel crystalline structure"
    },
    {
        "question": "Which of the following are true regarding enamel microabrasion?",
        "options": [
            "Indication is removal of superficial discolorations",
            "It is accomplished by using an acid and abrasive",
            "22 to 27 μm of enamel is removed with each treatment",
            "All the above are correct."
        ],
        "correct_answer": "All the above are correct."
    },
    {
        "question": "What technique can be used to create a matte finish and increase retention on the intaglio surface of a crown before cementation?",
        "options": [
            "Use of a fine diamond",
            "Use of a polishing disc",
            "HF acid",
            "Aluminum oxide air abrasion"
        ],
        "correct_answer": "Aluminum oxide air abrasion"
    },
    {
        "question": "The intaglio surface of a casting is best prepared by air-abrading the fitting surface with 50 um alumina. Alternative cleaning methods include steam cleaning, ultrasonics, and organic solvents.",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "First statement is true, second is false",
            "First statement is false, second is true"
        ],
        "correct_answer": "Both statements are true"
    },
    {
        "question": "The main advantage of lithium disilicate-containing ceramics relative to leucite-containing ceramics is their higher flexural strength and fracture toughness. The fabrication of fixed partial denture frameworks is possible with lithium disilicate-containing materials.",
        "options": [
            "The first statement is true, the second statement is false.",
            "The first statement is false, the second statement is true.",
            "Both statements are true.",
            "Both statements are false."
        ],
        "correct_answer": "Both statements are true."
    },
    {
        "question": "Which of the following is not true concerning enamel beveling for composite restorations:",
        "options": [
            "Bevels should be placed at an angle approximately 45 degrees to external tooth surface",
            "Rarely used for posterior composite restorations and not placed on areas of potential heavy occlusal forces, however Class I restorations may be beveled resulting in a 0.25-0.5 mm wide bevel.",
            "For moderate and large Class III beveled preparations, all accessible enamel margins are usually beveled, except for the gingival margin. No bevel should be placed on cementum.",
            "May enable the restoration to blend more esthetically with the coloration of the surrounding tooth structure",
            "All are true"
        ],
        "correct_answer": "All are true"
    },
    {
        "question": "When diagnosing anterior interproximal caries, which clinical method will lead to the most accurate and practical diagnosis?",
        "options": [
            "Use of orthodontic separators followed by tactile using an explorer",
            "Caries detection solution of methylene blue",
            "Fiber Optic Transillumination (FOTI)",
            "Use of the gold standard in caries detection - sectioning of teeth"
        ],
        "correct_answer": "Fiber Optic Transillumination (FOTI)"
    },
    {
        "question": "MCR crown is invested in which of the following investment material?",
        "options": [
            "Gypsum-bonded investment",
            "Quartz-bonded investment",
            "Phosphate-bonded investment",
            "Kaolin-bonded investment"
        ],
        "correct_answer": "Phosphate-bonded investment"
    },
    {
        "question": "Which of the following is true for posterior bucco-lingual embrasure form?",
        "options": [
            "The facial embrasure are usually larger than the lingual embrasure in a mandibular firs molar.",
            "The lingual embrasure are usually larger than the facial embrasure in a mandibular first molar.",
            "The facial embrasure is approximately equal to the lingual embrasure in a mandibular first molar.",
            "Embrasure form does not matter for the health of the periodontium."
        ],
        "correct_answer": "The lingual embrasure are usually larger than the facial embrasure in a mandibular first molar."
    },
    {
        "question": "\"Griffith flaws\" at the porcelain surface refers to",
        "options": [
            "Entrapped microscopic air pockets",
            "Minute cracks and scratches",
            "Voids incorporated into low-fusing porcelain during firing",
            "Gaps created when porcelain is treated with HF for more than 2 minutes"
        ],
        "correct_answer": "Minute cracks and scratches"
    },
    {
        "question": "Which of the following is incorrect regarding the use of resin cements used for cementation of all-ceramic crowns?",
        "options": [
            "The goal is to provide a marginal seal of the crown and adhesively retain it to the tooth",
            "Resin cementation is extremely technique sensitive",
            "It has been shown that a strong dependable bond between resin and ceramic can be achieved.",
            "The bond between dentin and the resin cement is stronger than the bond between the ceramic and the resin cement"
        ],
        "correct_answer": "The bond between dentin and the resin cement is stronger than the bond between the ceramic and the resin cement"
    },
    {
        "question": "In the advancing front of a demineralization zone, the dentinal tubules begin to have a crystalline precipation occur. When these affected tubules become completely occluded by the mineral precipitate what is the term to describe this zone.",
        "options": [
            "The Occluded zone",
            "The Transparent zone",
            "Dead tracts",
            "Sclerotic dentin"
        ],
        "correct_answer": "The Transparent zone"
    },
    {
        "question": "The following is considered the radiographic zones in caries: Outer Enamel (E1), Inner Enamel (E2), Outer Dentin (D1), and Inner Dentin (D2). According to Pitts (Car Res 96: 142) when caries reaches the outer dentin, it is cavitated 61% of the time",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "First statement is true, second is false",
            "First statement is false, second is true"
        ],
        "correct_answer": "First statement is true, second is false"
    },
    {
        "question": "Which of the following most accurately describes the mechanism by which aluminum compounds control bleeding?",
        "options": [
            "Precipitates proteins to physically obstruct hemorrhaging",
            "Coagulates blood by the classic mechanism",
            "Causes severe vasoconstriction of the local vasculature",
            "Induces rapid fibrotication of locally traumatized blood vessels"
        ],
        "correct_answer": "Precipitates proteins to physically obstruct hemorrhaging"
    },
    {
        "question": "The best technique for recording Centric Relation is?",
        "options": [
            "One-handed technique",
            "Record centric relation when the patient is upright",
            "The uppermost terminal axis must be delicately located in an open position without pressure on the mandible, and then it must be firmly held on that axis while the jaw is closed to the first point of contact. align the condyle-disk assemblies in the most superior position",
            "There is no one specific way that must be used to record centric relation correctly"
        ],
        "correct_answer": "There is no one specific way that must be used to record centric relation correctly"
    },
    {
        "question": "All of the following are reasons to perform a chair-side remount for major fixed case EXCEPT?",
        "options": [
            "There is a need for significant occlusal adjustment due to tooth movement",
            "To account for previous mounting discrepancies",
            "Intraoral occlusal adjustments are proven to be inadequate involving large fixed cases",
            "To account for dimensional changes inherent with the indirect process"
        ],
        "correct_answer": "Intraoral occlusal adjustments are proven to be inadequate involving large fixed cases"
    },
    {
        "question": "Which of the following are true in regards to the Law of Beams?  1. Double the height will cube the strength 2. Double the width will quadruple the strength 3. Half the height will diminish the strength by 1/4 4. Half the width will diminish the strength by 1/4",
        "options": [
            "1,3",
            "1,4",
            "2,3",
            "2,4"
        ],
        "correct_answer": "1,4"
    },
    {
        "question": "What happens to gypsum casts if it is soaked in non slurry water?",
        "options": [
            "Surface detail is lost.",
            "There is more porosity.",
            "The casts get weaker",
            "There is no difference between soaking the casts in slurry or non slurry water."
        ],
        "correct_answer": "Surface detail is lost."
    },
    {
        "question": "During #8-9 MCR try-in, the patient complains that the shade did not match her existing dentition and you decide correct it with custom staining. What is the most difficult to achieve?",
        "options": [
            "Decrease the hue",
            "Increase the hue",
            "Decrease chroma",
            "Decrease value"
        ],
        "correct_answer": "Decrease chroma"
    },
    {
        "question": "Raising the value of a ceramic restoration is almost impossible. However, lowering the value is done quite easily by adding the complementary color. Which of the following color combinations below are not complementary colors?",
        "options": [
            "Red, Green",
            "Violet, Yellow",
            "Blue, Orange",
            "Violet, Blue"
        ],
        "correct_answer": "Violet, Blue"
    },
    {
        "question": "Of the following machined dental ceramics which has the highest flexural strength?",
        "options": [
            "Alumina",
            "Feldspar",
            "Leucite",
            "Zirconia"
        ],
        "correct_answer": "Zirconia"
    },
    {
        "question": "Before cementing a porcelain veneer after try-in, you must treat the intaglio surface with which of the following?",
        "options": [
            "37% phosphoric acid",
            "37% hydrochloric acid",
            "15% phosphoric acid",
            "Silane coupling agent"
        ],
        "correct_answer": "Silane coupling agent"
    },
    {
        "question": "Typical film thickness of resin-based cements is less than that of traditional glass ionomer cements; however the 24-hour compressive strength of glass ionomer cements is typically greater than that of resin-based cements.",
        "options": [
            "The first statement is true, the second statement is false.",
            "The first statement is false, the second statement is true.",
            "Both statements are true.",
            "Both statements are false."
        ],
        "correct_answer": "Both statements are false."
    },
    {
        "question": "Which of the following is true regarding the overglazing of porcelain?",
        "options": [
            "Porcelain turns bluish grey",
            "Porcelain will fracture",
            "Porcelain turns black",
            "Unnatural shiny appearance"
        ],
        "correct_answer": "Unnatural shiny appearance"
    },
    {
        "question": "When considering ovate pontics and soft tissue development, all of the following apply EXCEPT?",
        "options": [
            "With a pre-existing healed ridge, there needs to be a minimum of 2.5 mm of gingival tissue over the ridge to allow for modification of soft tissue",
            "Ideally you want to create a concave pontic receptor site",
            "In dealing with these cases, one must consider preparation of the teeth (abutments) and the soft tissue",
            "With a pre-existing healed ridge, plasty tissues .5 - 1.0 mm followed by direct contact with the provisional"
        ],
        "correct_answer": "With a pre-existing healed ridge, there needs to be a minimum of 2.5 mm of gingival tissue over the ridge to allow for modification of soft tissue"
    },
    {
        "question": "Which of the following is true when restoring an endodontically treated tooth?",
        "options": [
            "If more than 2mm of coronal tooth structure remains, the post design has limited role in the fracture resistance of the restored tooth.",
            "Stresses are increased as post length increases",
            "Fiber made posts are advantageous in canals with noncircular cross sections or in canals with extreme taper",
            "Increasing the post diameter increased retention"
        ],
        "correct_answer": "If more than 2mm of coronal tooth structure remains, the post design has limited role in the fracture resistance of the restored tooth."
    },
    {
        "question": "Which of the following is true about investments and metals?",
        "options": [
            "Gypsum bonded materials are the investment of choice for metal-ceramic alloys because they are more stable at higher temperatures.",
            "Gypsum bonded materials are the investment of choice for metal-ceramic alloys because they are more stable at lower temperatures.",
            "Phosphate bonded materials are the investment of choice for metal-ceramic alloys because they are more stable at higher temperatures.",
            "Phosphate bonded materials are the investment of choice for metal-ceramic alloys because they are more stable at lower temperatures."
        ],
        "correct_answer": "Phosphate bonded materials are the investment of choice for metal-ceramic alloys because they are more stable at higher temperatures."
    },
    {
        "question": "Bis-acryl is often used for veneer provisional but retention may be challenging. What can be done to increase retention?",
        "options": [
            "Ensure the prep wraps around the lingual surface",
            "Create undercuts in the dentin",
            "Ensure the contacts are included in the prep",
            "Spot etch the enamel"
        ],
        "correct_answer": "Spot etch the enamel"
    },
    {
        "question": "When cementing a post with traditional cements, the choice of luting agents seems to have little effect on post retention. Resin cements have little effect on post performance.",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "The first is true and the second is false",
            "The first is false and the second is true"
        ],
        "correct_answer": "The first is true and the second is false"
    },
    {
        "question": "When applying die spacer, how far away should the die spacer stay away from the finish line?",
        "options": [
            "0.5mm to 1.0mm",
            "0.1mm to 0.3mm",
            "1.0mm to 1.5mm",
            "1.0mm to 2.0mm"
        ],
        "correct_answer": "0.5mm to 1.0mm"
    },
    {
        "question": "When preparing a MCR posterior crown a rationale for placing boxes on the facial and lingual is to counteract the lateral forces that result from the elliptical chewing motion. Grooves should be placed as parallel to the path of withdrawal as possible to maximize their effect.",
        "options": [
            "Both statements are true",
            "Both statements are false",
            "The first statement is true, the second is false",
            "The first statement is false, the second is true"
        ],
        "correct_answer": "The first statement is false, the second is true"
    },
    {
        "question": "Of the four proposed theories of porcelain-to-metal attachment, which is believed to be the most significant mechanism?",
        "options": [
            "Chemical bonding",
            "Mechanical interlocking",
            "Van Der Waal's forces",
            "Compression bonding"
        ],
        "correct_answer": "Chemical bonding"
    },
    {
        "question": "Which statement is not true for the Captek system for fabricating MCRs?",
        "options": [
            "The coping is produced from two metal-impregnated wax sheets that are adapted to a die and fired.",
            "First sheet forms a porous gold-platinum-palladium layer that is impregnated with 97% gold when the second sheet is fired.",
            "The limitation of Captek is the lack of ease of polishability and texture.",
            "Captek provides excellent esthetics and excellent marginal adaptation"
        ],
        "correct_answer": "The limitation of Captek is the lack of ease of polishability and texture."
    },
    {
        "question": "When considering FDP's and stress breakers, which of the following is NOT true?",
        "options": [
            "When considering a tilted molar as an abutment, axial tilt should not be > 25 degree",
            "With non-rigid connectors, mortise = matrix = female component",
            "The tenon = patrix = male component, is usually placed on the distal aspect of the anterior retainer (such as with a pier abutment)",
            "The mortise must parallel the path of withdrawal of the distal retainer."
        ],
        "correct_answer": "The tenon = patrix = male component, is usually placed on the distal aspect of the anterior retainer (such as with a pier abutment)"
    },
    {
        "question": "What is the maximum amount of anterior teeth that can be replaced between a pier abutment and a terminal abutment when restoring with fixed prosthesis?",
        "options": [
            "1",
            "2",
            "3",
            "4"
        ],
        "correct_answer": "4"
    },
    {
        "question": "What is the difference between an Arcon and Nonarcon articulator.",
        "options": [
            "In an arcon, the condylar spheres are attached to the upper member",
            "In a nonarcon, the condylar spheres are attached to the lower member",
            "In a nonarcon, the condylar spheres are attached to the upper member and lower member",
            "In an arcon, the condylar spheres are attached to the lower member"
        ],
        "correct_answer": "In an arcon, the condylar spheres are attached to the lower member"
    },
    {
        "question": "What is the purpose of the arbitrary facebow and how accurate can it be?",
        "options": [
            "Record and transfer the maxillary relationship to an arbitrary axis on the articulator with a minimum of 5 mm of error, usually in an anterioposterior direction",
            "Record and transfer both the maxillary and mandibular relationship to an arbitrary axis on the articulator with a minimum of 5 mm of error, usually in anterioposterior direction",
            "Record and transfer the mandibular relationship to an arbitrary axis on the articulator with a minimum of 11mm of error, usually in superior-inferior direction",
            "Record and transfer the maxillary relationship to an arbitrary axis on the articulator with a minimum of 13 mm of error, usually in inferior-posterior direction"
        ],
        "correct_answer": "Record and transfer the maxillary relationship to an arbitrary axis on the articulator with a minimum of 5 mm of error, usually in an anterioposterior direction"
    },
    {
        "question": "There are 2 types of facebows, ____________ and __________. The _________ is more accurate.",
        "options": [
            "Kinematic, Arbitrary, Kinematic",
            "Kinematic, Arbitrary, Arbitrary",
            "Arcon, Non-arcon, Arcon",
            "Arcon, Non-arcon, Non-Arcon"
        ],
        "correct_answer": "Kinematic, Arbitrary, Kinematic"
    },
    {
        "question": "Which of the following does not affect cusp height?",
        "options": [
            "Intercondylar width",
            "Condylar path inclination",
            "Mandibular lateral translation",
            "Angle of anterior guidance"
        ],
        "correct_answer": "Intercondylar width"
    },
    {
        "question": "What should be the expected increase in implant surface area available for osseointegration for every 1-mm increase in diameter (provided that body design remains identical)?",
        "options": [
            "5-10%",
            "15-25%",
            "35-45%",
            "55-65%"
        ],
        "correct_answer": "15-25%"
    },
    {
        "question": "Which type of bone could be described as a thick layer of cortical bone that surrounds a core of dense trabecular bone?",
        "options": [
            "Type I",
            "Type II",
            "Type III",
            "Type IV"
        ],
        "correct_answer": "Type II"
    },
    {
        "question": "When considering implants, which of the following statements is incorrect?",
        "options": [
            "With immediate implant placement, fixture should engage at least 5 mm of bone apically for primary stability",
            "Progressive loading is placement of a final prosthesis under immediate loading",
            "With immediate placement, the critical space between the platform and extraction socket should be < 2 mm and grafting is considered if > 1 mm",
            "Flatter incline planes and narrower occlusal tables create more vertical forces and a shorter moment arm"
        ],
        "correct_answer": "Progressive loading is placement of a final prosthesis under immediate loading"
    },
    {
        "question": "Meffert proposed conditions for implants, namely AILING, FAILING and FAILED. Ailing implants are those showing radiographical bone loss without inflammatory signs or mobility. Failing implants are those with progressive bone loss, signs of inflammation and mobility.",
        "options": [
            "The first part is true, the second part is false",
            "The first part is false, the second part is true",
            "Both statements are true",
            "Both statements are false"
        ],
        "correct_answer": "The first part is true, the second part is false"
    },
    {
        "question": "For a standard 3.75 implant, the minimum Buccal-lingual dimension is",
        "options": [
            "2 mm",
            "4 mm",
            "6 mm",
            "8 mm"
        ],
        "correct_answer": "6 mm"
    },
    {
        "question": "Implant retained overdentures that utilize attachment mechanisms such as bar-clip (such as Hader bar) will need a minimum interocclusal distance of",
        "options": [
            "5-7mm",
            "7-9mm",
            "10-12mm",
            "13-14mm"
        ],
        "correct_answer": "13-14mm"
    },
    {
        "question": "Implant retained overdentures that use individual attachments require a minimum occlusal distance of",
        "options": [
            "5-7mm",
            "7-9mm",
            "10-12mm",
            "12-14mm"
        ],
        "correct_answer": "10-12mm"
    },
    {
        "question": "Which of the following provides the most deleterious form of occlusal trauma in implants?",
        "options": [
            "Bruxism",
            "Severe clenching",
            "Shallow condylar inclination",
            "Shallow FMA angle"
        ],
        "correct_answer": "Bruxism"
    },
    {
        "question": "A potential problem of connecting natural teeth to implants is",
        "options": [
            "Failure of the natural tooth prosthesis",
            "Cement failure on the implant abutment",
            "Screw or abutment loosening",
            "Intrusion of the natural tooth"
        ],
        "correct_answer": "Intrusion of the natural tooth"
    },
    {
        "question": "What is the suggested cantilever length that can be extended either mesially or distally from an implant-supported FDP?",
        "options": [
            "0.5 to 0.75 times the anterior-posterior spread",
            "1.25 to 1.75 times the anterior-posterior spread",
            "2.0 to 2.5 times the anterior-posterior spread",
            "3.0 to 3.5 times the anterior-posterior spread"
        ],
        "correct_answer": "1.25 to 1.75 times the anterior-posterior spread"
    },
    {
        "question": "In determining the esthetic success of an implant, the gingival biotype of the implant site decisively influences:",
        "options": [
            "Contour, texture, transparency",
            "Size and color",
            "Gingival inflammation and plaque build up",
            "B and c"
        ],
        "correct_answer": "Contour, texture, transparency"
    },
    {
        "question": "With local anesthetic toxicity, all of the following are true, EXCEPT",
        "options": [
            "Most serious manifestations of local anesthesia toxicity are the appearance of generalized tonic-clonic seizure activity and cardiac depression",
            "Moderate toxicity can manifest with headache, dizziness, and blurred vision",
            "Diazepam (valium) 5-10 mg should be administered slowly with extreme toxicity",
            "11 carpules of 2% Lido w/ 1:100,000 epi can safely be administered to a 50kg individual"
        ],
        "correct_answer": "11 carpules of 2% Lido w/ 1:100,000 epi can safely be administered to a 50kg individual"
    },
    {
        "question": "Clinical presentation of a zygoma fracture includes which of the following?  A) Clinical flattening or the cheekbone prominence B) Mobile maxilla C) Paraesthesia in distribution area of inferior alveolar nerve D) Floor of mouth hematoma E) All the above A) Clinical flattening or the cheekbone prominence The most diagnostic radiograph for a maxillary fracture is",
        "options": [
            "Cone Beam CT",
            "Panograph",
            "PA Ceph",
            "Lateral Ceph"
        ],
        "correct_answer": "Cone Beam CT"
    },
    {
        "question": "After a mandibular 3rd molar extraction, you examined the tooth and noticed the distal root is fractured and not present in the socket, what is the most likely area the root tip is displaced?",
        "options": [
            "Oropharynx",
            "Submandibular fascial space",
            "Sublingual fascial space",
            "Submental space"
        ],
        "correct_answer": "Submandibular fascial space"
    },
    {
        "question": "Which part of the mandible has the highest incidence of fracture?",
        "options": [
            "Angle",
            "Body",
            "Ramus",
            "Condyle"
        ],
        "correct_answer": "Condyle"
    },
    {
        "question": "Where is the film located when taking a Waters view radiograph?",
        "options": [
            "Directly in front",
            "Directly behind",
            "In front with a 37 degree angle",
            "In front with a -30 degree angle"
        ],
        "correct_answer": "In front with a 37 degree angle"
    },
    {
        "question": "The most common space that is involved when erosion of the lingual plate adjacent to tooth #20 occurs is the:",
        "options": [
            "Sublingual space or submandibular space",
            "Mental space",
            "Buccal space",
            "Pterygomandibular space"
        ],
        "correct_answer": "Sublingual space or submandibular space"
    },
    {
        "question": "F. The first statement is false, the second statement is true. G. Both statements are true. H. Both statements are false. G. Both statements are true. When you have an impacted Maxillary 3rd molar what is the most common facial space that is involved?",
        "options": [
            "Temporal space",
            "Buccal space",
            "Infratemporal space",
            "Lateral Pterygomandibular space"
        ],
        "correct_answer": "Infratemporal space"
    },
    {
        "question": "All of the following statements concerning cavernous sinus thrombosis (CST) are true EXCEPT",
        "options": [
            "Bacteria may travel from the maxilla posteriorly via the pterygoid plexus and emissary veins to the cavernous sinus",
            "Staphylococcus aureus and streptococcus are often the associated bacteria with CST",
            "Bacteria may travel from the maxilla anteriorly via the angular vein and inferior/superior ophthalmic veins to the cavernous sinus",
            "CST may occur as the result of inferior spread of odontogenic infection via a hematogenous route"
        ],
        "correct_answer": "CST may occur as the result of inferior spread of odontogenic infection via a hematogenous route"
    },
    {
        "question": "The use of Dexamethasone is recommended to do all the following except?",
        "options": [
            "Reduce postoperative nausea and vomiting",
            "Reduce pain",
            "Enhance wound healing",
            "Reduce inflammation"
        ],
        "correct_answer": "Enhance wound healing"
    },
    {
        "question": "Hematomas are most associated with which of the following blocks?",
        "options": [
            "Greater Palatine",
            "Posterior Superior Alveolar",
            "Middle Superior Alveolar",
            "Mental"
        ],
        "correct_answer": "Posterior Superior Alveolar"
    },
    {
        "question": "Upon histologic examination this condition presents with hyperparakeratosis, spongiosis, acanthosis, and elongation of the epithelial rete ridges.",
        "options": [
            "Fissured tongue",
            "Benign migratory glossitis",
            "Lichen planus",
            "White sponge nevus"
        ],
        "correct_answer": "Benign migratory glossitis"
    },
    {
        "question": "When looking at root formation when is the best time to remove third molars?",
        "options": [
            "Completely formed",
            "1/3 to 2/3 formed",
            "¾ to 5/6th formed",
            "6/7 to 7/8 formed"
        ],
        "correct_answer": "1/3 to 2/3 formed"
    },
    {
        "question": "A patient presents as an emergency, with noticeable swelling below tooth #28. His blood pressure readings are as follows: Initial: 182/120; 2nd reading (5 minutes after 1st): 185/110; 3rd reading (5 minutes after 2nd): 180/105. What would be your treatment?",
        "options": [
            "Extract #28 or begin NSRCT/I&D, refer patient to primary care physician",
            "Extract #28 or begin NSRCT/I&D, refer patient to nearest emergency room",
            "Refer patient to nearest emergency room"
        ],
        "correct_answer": "Extract #28 or begin NSRCT/I&D, refer patient to primary care physician"
    },
    {
        "question": "Which of the following extraoral radiographs best indicated when assessing suspected fractures of the orbit and zygoma?",
        "options": [
            "Reverse Towne",
            "Lateral Ramus",
            "Panoramic",
            "Waters"
        ],
        "correct_answer": "Waters"
    },
    {
        "question": "Which of the following are true concerning Battle's sign?",
        "options": [
            "Occurs with-in the first 30 minutes of trauma",
            "Consists of bruising around the mastoid process and may indicate a middle fossa skull fracture or leakage of blood from a condylar fracture or trauma to the auditory canal",
            "Consists of bilateral circumorbital ecchymoses, nasal epistaxis and CSF rhinorrhea and indicates a skull fracture in the anterior fossa.",
            "Occurs from blast damage that causes rapid expansion of gas in internal hollow organs"
        ],
        "correct_answer": "Consists of bruising around the mastoid process and may indicate a middle fossa skull fracture or leakage of blood from a condylar fracture or trauma to the auditory canal"
    },
    {
        "question": "When discussing odontogenic infections, which statement is false?",
        "options": [
            "The majority of causative organisms of odontogenic infections are mixed aerobic/anaerobic (65%)",
            "Gram + cocci, such as streptococcus pyogenes, represent the major aerobic organism causing odontogenic infections",
            "Cellulitis is highly associated with aerobic bacteria",
            "Duration of cellulitis is classified as chronic"
        ],
        "correct_answer": "Duration of cellulitis is classified as chronic"
    },
    {
        "question": "Which of the following antibiotics is most commonly associated with pseudomembranous colitis?",
        "options": [
            "Metronidazole",
            "Sulfonamides",
            "Quinolones",
            "Tetracyclines"
        ],
        "correct_answer": "Quinolones"
    },
    {
        "question": "A patient presents with complaint of a boney spicule one week after the extraction of #18. What would you do to treat the patient?",
        "options": [
            "With no pain and swelling, place patient on antibiotics and analgesics and wait for the boney spicule to exfoliate.",
            "With pain and swelling, leave it alone, the boney spicule may erupt on its own.",
            "With no pain and swelling, reopen extraction site and allow to exfoliate",
            "With pain and extraoral swelling, place the patient on antibiotics and analgesics, then after the swelling has resolved, remove the boney spicule with rongeurs"
        ],
        "correct_answer": "With pain and extraoral swelling, place the patient on antibiotics and analgesics, then after the swelling has resolved, remove the boney spicule with rongeurs"
    },
    {
        "question": "The most common site for exposed bone/alveolar osteitis post extraction is",
        "options": [
            "Maxillary impacted canine region",
            "Maxillary tuberosity area",
            "Mandibular impacted premolars",
            "Mandibular impacted 3rd molars",
            "Probability is highest if patient is a smoker and if the extraction was traumatic, so all sites have similar probability."
        ],
        "correct_answer": "Mandibular impacted 3rd molars"
    }
]

def copy_to_clipboard(text):
    """Cross-platform clipboard copy function"""
    try:
        # Try Pythonista's clipboard first
        import clipboard
        clipboard.set(text)
        return True
    except ImportError:
        try:
            # Try pyperclip for desktop
            import pyperclip
            pyperclip.copy(text)
            return True
        except ImportError:
            return False

def format_question(question_data):
    """Format the question with emoji prefixes"""
    emojis = ['❤️', '👍', '👎', '😂', '👏', '🙌', '✅', '⭐']  # Updated common emojis
    
    # Get the question and options
    question_text = question_data["question"]
    options = question_data["options"].copy()
    correct_answer = question_data["correct_answer"]
    
    # Shuffle the options
    random.shuffle(options)
    
    # Format the clipboard text (without correct answer)
    clipboard_text = f"Gum Guess of the Day!\n\n{question_text}\n\n"
    
    # Format the display text (with correct answer)
    display_text = clipboard_text
    
    # Keep track of which emoji was used for the correct answer
    correct_answer_emoji = None
    
    # Add emoji prefixes to options
    for emoji, option in zip(emojis, options):
        clipboard_text += f"{emoji} {option}\n"
        display_text += f"{emoji} {option}\n"
        if option == correct_answer:
            correct_answer_emoji = emoji
    
    # Add the correct answer only to display text
    display_text += f"\nCorrect Answer: {correct_answer_emoji} {correct_answer}"
    
    return clipboard_text, display_text, options

def main():
    if not QUESTIONS:
        print("No questions available!")
        return
    
    # Get a random question
    question_data = random.choice(QUESTIONS)
    
    # Format the question and get shuffled options
    clipboard_text, display_text, shuffled_options = format_question(question_data)
    
    # Try to copy to clipboard
    if copy_to_clipboard(clipboard_text):
        print("\nQuestion copied to clipboard!")
    else:
        print("\nNote: Clipboard functionality not available.")
    
    # Print the full text including correct answer
    print("\n" + display_text)

if __name__ == "__main__":
    main()
