# EMA Hourly Continuation — UMA/USDT P20_55

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 911 |
| net_profit_factor | 0.5083 |
| net_win_rate | 0.4610 |
| gross_profit_factor | 0.8896 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -6.0847 |
| sortino_ratio | -2.6076 |
| max_drawdown | 0.9559 |
| cagr | -0.7088 |
| net_avg_win | 23.5019 |
| net_avg_loss | -39.5506 |
| avg_hold_time_bars | 6.5840 |
| exposure | 0.2726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
