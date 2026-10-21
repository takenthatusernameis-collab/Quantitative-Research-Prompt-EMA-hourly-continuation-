# EMA Hourly Continuation — BOME/USDT P50_55

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.7288 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9517 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.1037 |
| sortino_ratio | -0.1752 |
| max_drawdown | 0.2338 |
| cagr | -0.0773 |
| net_avg_win | 81.9295 |
| net_avg_loss | -107.0647 |
| avg_hold_time_bars | 4.4797 |
| exposure | 0.0250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
