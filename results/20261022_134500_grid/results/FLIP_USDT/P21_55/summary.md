# EMA Hourly Continuation — FLIP/USDT P21_55

**Symbol:** FLIP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.4117 |
| net_win_rate | 0.4090 |
| gross_profit_factor | 0.7941 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -7.2295 |
| sortino_ratio | -2.5864 |
| max_drawdown | 0.9635 |
| cagr | -0.7291 |
| net_avg_win | 25.4154 |
| net_avg_loss | -42.7124 |
| avg_hold_time_bars | 9.5139 |
| exposure | 0.2802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
