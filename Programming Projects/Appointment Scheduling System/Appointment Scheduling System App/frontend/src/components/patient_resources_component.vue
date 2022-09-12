<template>
    <div id="patientResourcesComponentBody" style="min-height: 95vh;">
        
      <div class="mx-auto" style="box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);width: 75%; min-width: 290px; max-width: 1050px; padding-top: 50px; padding-bottom: 50px;">
         <div class="row mx-auto mb-1" id="textArea" style="margin-top: 4%;">
            <h1 class="mb-0">Patient resources (FAQ)</h1>
            <p>
               An important aspect of dentistry is patient education. Here at Smile Architects, we believe that providing patients with excellent service is only half the story. Understanding what dentistry is and how it is performed is beneficial for both the patients and providers. 
            </p>
            <select v-model="this.selection"  class="form-select mb-4" aria-label="Default select example" style="width: 95%; margin-left: 10px;">
               <option>General FAQ</option>
               <option>Orthodontics FAQ</option>
            </select>
         </div>

         
         <div v-if="this.selection == 'General FAQ'">
   
            <div class="mx-auto mb-1" style="border-style: solid; width: 72.7%; min-width: 260px; max-width: 780px; border-radius: 10px; border-color: #292b2c;"></div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px; box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Do we normally accept walk in patients?</div>
                        <p  class="mt-4">
                           We accept walk in patients but it depends on the schedule and if it is an emergency; schedule patients have priority. If it is too busy, we will have to ask you to schedule an appointment on a later date. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">When do I need to see a dentist?</div>
                        <p  class="mt-4">
                           You typically see the dentist for a regular cleaning or when you have any concerns about your oral health. It is generally recommended to see a dentist for a cleaning every 6 months. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">When do I have to see a specialist?</div>
                        <p  class="mt-4">
                           You will usually be referred to a specialist by your dentist when a certain procedure requires someone in that field.  
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Are extractions typically painful?</div>
                        <p  class="mt-4">
                           Extractions should virtually be pain free once the anesthetic set in. You will feel pressure but there should be no pain felt during the operation.    
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How often do I need to brush my teeth and floss?</div>
                        <p  class="mt-4">
                           It is recommended you brush at least twice a day and floss once a day. This to ensure that the oral cavity is clean to prevent any infection or bacterial growth. Flossing is important because brushing does not reach in between the teeth or gum where food particles can be trapped.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Why do I need my wisdom teeth removed?</div>
                        <p  class="mt-4">
                           Wisdom teeth can grow in wrong and that can cause problems. They can grow in at an angle, and in some cases, horizontally. This causes an impact with the other molars, resulting in pain and other complications.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How much do I have to pay for a certain service?</div>
                        <p  class="mt-4">
                           An accurate estimate cannot be given until after an oral evaluation is given. The dentist will have to see if there are any concerns and the severity of any complications.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What do I do after oral surgery and how long to heal?</div>
                        <p  class="mt-4">
                           After oral surgery, you should bite onto the gauze until the area stops bleeding; this can take a few hours and the gauze should be replaced about every hour. After the bleeding stops, avoid drinking through straws, rinsing your mouth (first 24 hours), spitting, rigorous activities, and chewing in that area. You want to avoid the surgical area until it heals adequately. Eat soft food and gradually move back to a normal diet. Depending on the surgery, the area will heal in a week or two. Make sure to keep your mouth clean and eat a proper diet to recover as fast as possible. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How do I prevent staining on my teeth?</div>
                        <p  class="mt-4">
                           One of the most common things that causes staining on teeth is food and drinks; coffee is a prime example. The best way to avoid staining your teeth is to reduce the amount of things in your diet that can cause staining. Having proper oral hygiene also helps prevent stains. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What is the bone grafting material made from?</div>
                        <p  class="mt-4">
                           The bone grafting material can be made from your own bone or a variety of material that is compatible with the body. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Why do I need a root canal?</div>
                        <p  class="mt-4">
                           A root canal therapy is needed when there is an infected pulp, the center of the tooth where the nerves and blood vessels are; the infected pulp is removed to avoid anymore complications that can occur. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What do I do if part of my tooth breaks off?</div>
                        <p  class="mt-4">
                           If you teeth happens to break off, try to hold onto the fragment(s) and bring it with you to the dentist. Depending on how severe the the it is, you may feel pain since the tooth is exposed. Try to avoid getting the area infected and take pain reliever if necessary. The dentist can offer you different solutions depending on the problem. If it's a minor chip, the tooth can be smoothed out. If it is more major, a composite or crown might be required to reconstruct the tooth.
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Why do I need a deep cleaning?</div>
                        <p  class="mt-4">
                           Also known as scaling and root planning, you need a deep cleaning when there is a build up of dental plaque and calculus on the teeth. They can cause inflammation and other problems. Removing the tartar is essential for good gum and overall oral health. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Is it normal to bleed when brushing/flossing my teeth?</div>
                        <p  class="mt-4">
                           If you are experience constant bleeding when brushing your teeth, it is advised to see a dentist to ensure you don't not have a periodontal disease or gingivitis. If you are flossing and there is mild bleeding, it is usually because you just started flossing. The bleeding will stop after routine brushing and flossing, improving the gum health.  
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-5">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Should I rinse with mouthwash every day?</div>
                        <p  class="mt-4">
                           Rinsing with mouthwash is an optional thing. Only brushing and flossing is actually necessary, but if you want an extra bit of cleaning or freshening, make sure to use the product correctly for optimal results. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>
         </div>









          <div v-if="this.selection == 'Orthodontics FAQ'">
            <div class="mx-auto mb-1" style="border-style: solid; width: 72.7%; min-width: 260px; max-width: 780px; border-radius: 10px; border-color: #292b2c;"></div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px; box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How long do I have to wear braces for?</div>
                        <p  class="mt-4">
                           The amount of time needed for braces varies between each individual. A variety of factors determine the length of braces; they range from how crowded the teeth are to the age of the patient.  
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">Does wearing braces hurt?</div>
                        <p  class="mt-4">
                           Generally, you will feel pressure from the wires as they are adjusted to move the teeth. However, no sharp pain should ever occur. If that does happen, it is most likely from the wires poking your mouth. They can be easily trimmed at your next appointment. In the meantime, if it is bothering you too much, you can put a bit of wax, that was given to you, on it.  
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How much will braces cost?</div>
                        <p  class="mt-4">
                           Before an estimate can be given, the patient should first have a consultation with an orthodontist.  
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What can't I eat while wearing braces?</div>
                        <p  class="mt-4">
                           The main food to avoid while wearing braces are hard and sticky food. Things like corn chip and nuts can break/loosen the brackets or bend the wire. Sticky candy or gum can also loosen the brackets. You generally want to avoid biting hard things head on. For example, you can eat apples, but try to cut them into bite size pieces first.  
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How do I get regular cleanings at the dentist when I have braces on?</div>
                        <p  class="mt-4">
                           Before a regular cleaning, the orthodontist will remove the metal wire. After the dentist clean your teeth, the wires will be placed back on. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">How do I brush and floss my teeth with braces?</div>
                        <p  class="mt-4">
                           You have to brush very thoroughly because food particle can easily be trapped in the brackets and wire. You should angle your toothbrush so it can cover the top and bottom of the braces. You will also need a floss threader to get behind the wires; you just floss normally after that. If food is still stuck in the braces, you may need a proxabrush to get it out.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">When do I have to wear my retainer(s)?</div>
                        <p  class="mt-4">
                           After you get your braces removed, you typically wear your retainer constantly for a set amount of months (determined by the orthodontist). After that allotted time period, you would wear your retainers at night only. This is to ensure that your teeth stays in the corrected position.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>
            
            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What happens if I lose my retainer(s)?</div>
                        <p  class="mt-4">
                           Your teeth will begin to move after your braces are removed so it is important to wear your retainer(s) daily. If you happen to lose it, go to your orthodontist as soon as possible so that a new one can be made. 
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What do I do if a bracket gets loose/break or if I lose it?</div>
                        <p  class="mt-4">
                           If a bracket happens to get loose or breaks off, just hold on to it. The orthodontist will put it back on when you come in for your next appointment.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-3">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What is the age limit for braces?</div>
                        <p  class="mt-4">
                           There is no real age limit for braces, but generally, the younger the better. The teeth can be more easily corrected at a young age and the bone can facilitate the movement better.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>

            <div class="row mx-auto mb-3" id="textArea">
               <div class="row mt-4 mb-5">
                  <div class="col">
                     <div>
                        <div class="bg-dark text-white p-2" style="padding-top: 3px; margin-left: 0px;  height: 100%; width: 100%; font-size: min(6vw, 25px); border-radius: 10px;  box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);">What happens if I don't wear my retainer(s)?</div>
                        <p  class="mt-4">
                           After your braces are removed, your teeth will begin to move unless you wear your retainers. If you do not, it will move out of the corrected position and you may have to get braces again to fix it. You can notice the effect of not wearing a retainer in a short period of time. If you skip, the retainer may be tighter the next time you try to put it on.   
                        </p>
                     </div>
                  </div>
               </div>    
            </div>
         </div>


      </div>
    </div>
</template>

<script>
export default {
        name: 'patient_resources_component',
        data() {
           return {
              selection: 'General FAQ'
           }
        },
        methods: {
           changeSelection() {
              if (this.selection == 'General FAQ') {
                 this.selection = 'Orthodontics FAQ'
              }
              if (this.selection == 'Orthodontics FAQ') {
                 this.selection = 'General FAQ'
              }
           }
        }
}
</script>

<style scoped>
#textArea {
  margin-bottom: 12%;
  width: 75%;
  min-width: 290px;
  max-width: 800px;
}

img {
    width: 100%;
    max-width: 600px;
    min-width: 250px;
    box-shadow: 0 1px 5px rgb(0 0 0 / 0.4);
}

p {
    font-size: min(5.5vw, 20px);
}
</style>