# EMA Hourly Continuation — RENDER/USDT P12_50

**Symbol:** RENDER/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.7875 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 0.9962 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.8779 |
| sortino_ratio | -0.6955 |
| max_drawdown | 0.5506 |
| cagr | -0.2752 |
| net_avg_win | 64.0808 |
| net_avg_loss | -82.5127 |
| avg_hold_time_bars | 8.9757 |
| exposure | 0.2729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
