# EMA Hourly Continuation — MTL/USDT P26_100

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.6284 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8412 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -3.4121 |
| sortino_ratio | -1.0350 |
| max_drawdown | 0.7105 |
| cagr | -0.3812 |
| net_avg_win | 57.6183 |
| net_avg_loss | -74.9568 |
| avg_hold_time_bars | 20.8319 |
| exposure | 0.4318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
