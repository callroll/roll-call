<script setup>
import {useInstallationStore} from "@/store/installationstore";

import {useRoute, useRouter} from "vue-router";
import {useTableStore} from "@/store/tablestore";

const emitter = defineEmits(["changedV"]);
const changed =  async function changed() {


  if (route.params.installationId){

    const newParams ={ installationId: installationStore.chosenInstallation};
    const currentParams = route.params;
    route.params.installationId = installationStore.chosenInstallation;
    const mergedParams = { ...currentParams, newParams };
//    await tableStore.getOccupants();
    //tableStore.items = installationStore.occupants
    router.push({ params: mergedParams });

  }


};
const installationStore = useInstallationStore();

const tableStore = useTableStore();
</script>
<script>

var router = null;
var route = null;
import {useInstallationStore} from "@/store/installationstore";



export  default {
  name: "InstallationChooser",

   mounted() {
    route = this.$route;
    router = this.$router;
    const installationStore = useInstallationStore();
    const tableStore = useTableStore();
    installationStore.getInstallations();

    if (this.$route.params.installationId &&  (typeof installationStore.chosenInstallation != 'undefined' ||installationStore.chosenInstallation !='' )){
      installationStore.chosenInstallation = this.$route.params.installationId;

    }

  }



}
</script>
<template>
<div><v-select v-model="installationStore.chosenInstallation" @update:menu="changed" :items="installationStore.installations" item-value="id" item-title="name" >

</v-select></div>
</template>
