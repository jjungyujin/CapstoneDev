<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import mainDashboard from "../../components/mainDashboard";
import mainInputTableHeader from "../../components/mainInputTableHeader";
import mainInputTable from "../../components/mainInputTable";
import resetButton from "../../components/resetButton";
import mainFooter from "../../components/mainFooter";

export default {
  components: {
    mainHeader,
    mainNav,
    mainDashboard,
    mainInputTableHeader,
    mainInputTable,
    resetButton,
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
          <div class="card mb-4">
            <mainInputTableHeader />
            <mainInputTable />
            <resetButton />
          </div>
        </div>
        <mainFooter />
      </div>
    </div>
  </div>
</template>
