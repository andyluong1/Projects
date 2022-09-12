<template>
    <div id="contactUsComponentBody" style="min-height: 95vh;">
        <div class="mx-auto" style="box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);width: 75%; min-width: 290px; max-width: 1050px; padding-top: 50px; padding-bottom: 50px;">

            <div class="row mx-auto mb-1" id="textArea" style="margin-top: 4%;">
                <h1 class="mb-0">Ask us a question</h1>
                <p>
                Your concerns and questions are important to us so feel free to ask us anything. You can either message us by email or call us at 281-498-1100 during our normal business hours. For more details, see below.
                </p>
            </div>

            <div class="mx-auto mb-1" style="border-style: solid; width: 72.7%; min-width: 260px; max-width: 780px; border-radius: 10px; border-color: #292b2c;"></div>
            
            <div class="row mx-auto mt-5 mb-5" id="textArea" style="min-height: 400px;">
                <GMapMap style="width: 500px; height: 400px; box-shadow: 0 0px 5px rgb(0 0 0 / 0.4);"
                    :center="center"
                    :zoom="14"
                    map-type-id="terrain"
                >
                <GMapCluster>
                <GMapMarker
                    :key="index"
                    v-for="(m, index) in markers"
                    :position="m.position"
                    :clickable="true"
                    :draggable="true"
                    @click="center=m.position"
                />
                </GMapCluster>
                </GMapMap>  
            </div>
        
            <div class="mx-auto mb-1" style="border-style: solid; width: 72.7%; min-width: 260px; max-width: 780px; border-radius: 10px; border-color: #292b2c;"></div>

            <div class="row mx-auto mb-2" id="textArea">
                <div class="row mt-3 mb-3">
                    <div class="col mt-2">
                    <div>
                        <p class="fw-bold">Office Hours:</p>
                        <p>Monday 10 AM - 6 PM</p>
                        <p>Tuesday 10 AM - 6PM</p>
                        <p>Wednesday Closed </p>
                        <p>Thursday 10 AM - 6 PM</p>
                        <p>Friday 10 AM - 6 PM</p>
                        <p>Saturday 9AM - 3 PM</p>
                        <p>Sunday Closed</p>
                        
                    </div>
                    </div>
                    <div class="col mt-2">
                        <p class="fw-bold">Office contact information</p>
                        <p>11322 Bellaire Blvd #112 Houston, TX 77072</p>
                        <p>smilearchitects1100@yahoo.com</p>
                        <p>(Phone) 281.498.1100</p>
                        <p>(Fax) 281.498.1102</p>
                    </div>
                </div>    
            </div>
        </div>
    </div>
</template>

<script>

export default {
        name: 'contact_us_component',
        data() {
            return {
                center: {lat: 29.704367426606705, lng: -95.57812450241961},
                markers: [{
                    position: {
                        lat: 29.704367426606705, lng: -95.57812450241961
                    },
                }]
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

p {
    font-size: min(5.5vw, 20px);
}
</style>
