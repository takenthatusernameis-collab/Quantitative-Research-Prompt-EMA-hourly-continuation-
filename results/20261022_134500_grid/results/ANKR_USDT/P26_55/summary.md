# EMA Hourly Continuation — ANKR/USDT P26_55

**Symbol:** ANKR/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 926 |
| net_profit_factor | 0.4760 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.8986 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -8.6152 |
| sortino_ratio | -3.7195 |
| max_drawdown | 0.9905 |
| cagr | -0.8416 |
| net_avg_win | 23.0678 |
| net_avg_loss | -35.2587 |
| avg_hold_time_bars | 5.2624 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
