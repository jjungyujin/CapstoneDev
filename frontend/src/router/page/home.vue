<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import mainDashboard from "../../components/mainDashboard";
import mainFooter from "../../components/mainFooter";

export default {
  components: {
    mainHeader,
    mainNav,
    mainDashboard,
    mainFooter
  }
};
</script>

<template>
  <div>
    <mainHeader />
    <div id="layoutSidenav">
      <mainNav />
      <div id="layoutSidenav_content">
        <mainDashboard />
        <mainFooter />
      </div>
    </div>
  </div>
</template>
