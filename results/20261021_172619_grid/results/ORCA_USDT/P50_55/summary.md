# EMA Hourly Continuation — ORCA/USDT P50_55

**Symbol:** ORCA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 181 |
| net_profit_factor | 0.6236 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.9705 |
| sortino_ratio | -0.3810 |
| max_drawdown | 0.3840 |
| cagr | -0.1597 |
| net_avg_win | 65.9184 |
| net_avg_loss | -102.2560 |
| avg_hold_time_bars | 6.2597 |
| exposure | 0.0515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
