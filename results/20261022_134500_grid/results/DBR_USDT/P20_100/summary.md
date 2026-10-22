# EMA Hourly Continuation — DBR/USDT P20_100

**Symbol:** DBR/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 497 |
| net_profit_factor | 0.4756 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.7564 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -5.4380 |
| sortino_ratio | -1.9077 |
| max_drawdown | 0.8460 |
| cagr | -0.6028 |
| net_avg_win | 35.5737 |
| net_avg_loss | -57.0251 |
| avg_hold_time_bars | 14.8592 |
| exposure | 0.4200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
