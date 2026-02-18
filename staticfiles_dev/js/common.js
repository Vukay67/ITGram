// =========================
    // Theme toggle (light/dark)
    // =========================
    const root = document.documentElement;
    const themeToggle = document.getElementById("themeToggle");

    // Restore theme
    const savedTheme = localStorage.getItem("itgram-theme");
    if (savedTheme === "dark" || savedTheme === "light") {
      root.setAttribute("data-theme", savedTheme);
    }

    themeToggle.addEventListener("click", () => {
      const cur = root.getAttribute("data-theme") || "light";
      const next = cur === "light" ? "dark" : "light";
      root.setAttribute("data-theme", next);
      localStorage.setItem("itgram-theme", next);
    });

    // =========================
    // Stories modal open/close
    // =========================
    const modal = document.getElementById("storyModal");
    const closeBtn = document.getElementById("closeStory");

    const storyImg = document.getElementById("storyImg");
    const storyUser = document.getElementById("storyUser");
    const storyName = document.getElementById("storyName");
    const storyText = document.getElementById("storyText");
    const storyUserPic = document.getElementById("storyUserPic");

    function openStory({ user, name, text, img }) {
      storyImg.src = img;
      storyUser.textContent = user;
      storyName.textContent = name;
      storyText.textContent = text;

      // Slightly vary userpic gradient based on user
      const hue = Math.abs(hashCode(user)) % 360;
      storyUserPic.style.background = `linear-gradient(135deg, hsl(${hue} 90% 60%), var(--brand-1))`;

      modal.setAttribute("open", "");
      modal.setAttribute("aria-hidden", "false");
      document.body.style.overflow = "hidden";
    }

    function closeStory() {
      modal.removeAttribute("open");
      modal.setAttribute("aria-hidden", "true");
      document.body.style.overflow = "";
      storyImg.src = "";
    }

    closeBtn.addEventListener("click", closeStory);
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeStory();
    });
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && modal.hasAttribute("open")) closeStory();
    });

    document.querySelectorAll(".story").forEach((el) => {
      el.addEventListener("click", () => {
        openStory({
          user: el.getAttribute("data-story-user") || "@user",
          name: el.getAttribute("data-story-name") || "User",
          text: el.getAttribute("data-story-text") || "",
          img: el.getAttribute("data-story-img") || "https://picsum.photos/seed/itgram_story_fallback/1200/900",
        });
      });
    });

    function hashCode(str) {
      let h = 0;
      for (let i = 0; i < str.length; i++) h = (h << 5) - h + str.charCodeAt(i) | 0;
      return h;
    }

    // =========================
    // Demo likes (toggle + count)
    // =========================
    document.querySelectorAll("[data-like]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const countEl = btn.querySelector("[data-like-count]");
        if (!countEl) return;

        const liked = btn.getAttribute("data-liked") === "1";
        const n = parseInt((countEl.textContent || "0").replace(/[^\d]/g, ""), 10) || 0;

        const nextLiked = !liked;
        btn.setAttribute("data-liked", nextLiked ? "1" : "0");

        // simple +1/-1
        const next = nextLiked ? n + 1 : Math.max(0, n - 1);
        countEl.textContent = next.toLocaleString("ru-RU");

        // subtle visual
        btn.style.borderColor = nextLiked ? "color-mix(in oklab, var(--brand-1) 60%, var(--border))" : "";
        btn.style.background = nextLiked ? "color-mix(in oklab, var(--brand-1) 18%, transparent)" : "";
      });
    });