# EMA Hourly Continuation — CAKE/USDT P8_20

**Symbol:** CAKE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.7168 |
| net_win_rate | 0.5144 |
| gross_profit_factor | 1.0719 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -2.4892 |
| sortino_ratio | -0.8191 |
| max_drawdown | 0.6197 |
| cagr | -0.3122 |
| net_avg_win | 57.5358 |
| net_avg_loss | -85.0308 |
| avg_hold_time_bars | 5.8714 |
| exposure | 0.1390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
