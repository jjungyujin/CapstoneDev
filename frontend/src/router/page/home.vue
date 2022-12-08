<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import mainDashboard from "../../components/mainDashboard";
import mainInputTable from "../../components/mainInputTable";
import mainFooter from "../../components/mainFooter";

export default {
  components: {
    mainHeader,
    mainNav,
    mainDashboard,
    mainInputTable,
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
        <div class="container-fluid px-4">
          <mainDashboard />
          <mainInputTable />
        </div>
        <mainFooter />
      </div>
    </div>
  </div>
</template>
