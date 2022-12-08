<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import mainDashboard from "../../components/mainDashboard";

export default {
  components: {
    mainHeader,
    mainNav,
    mainDashboard
  }
};
</script>

<template>
  <div>
    <mainHeader />
    <div id="layoutSidenav">
      <mainNav />
      <mainDashboard />
    </div>
  </div>
</template>
