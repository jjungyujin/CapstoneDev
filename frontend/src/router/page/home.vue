<script>
import mainHeader from "../../components/mainHeader";
import mainNav from "../../components/mainNav";
import mainInputTable from "../../components/mainInputTable";
import mainFooter from "../../components/mainFooter";

export default {
  components: {
    mainHeader,
    mainNav,
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
        <mainInputTable />
        <mainFooter />
      </div>
    </div>
  </div>
</template>
