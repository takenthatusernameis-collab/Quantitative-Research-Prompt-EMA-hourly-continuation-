# EMA Hourly Continuation — SWFTC/USDT P21_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4458 |
| gross_profit_factor | 0.8665 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -4.0402 |
| sortino_ratio | -1.2634 |
| max_drawdown | 0.7870 |
| cagr | -0.4548 |
| net_avg_win | 55.6129 |
| net_avg_loss | -73.0666 |
| avg_hold_time_bars | 23.4357 |
| exposure | 0.5305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
