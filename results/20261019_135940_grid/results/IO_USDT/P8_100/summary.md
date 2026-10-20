# EMA Hourly Continuation — IO/USDT P8_100

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6297 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8650 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -4.0706 |
| sortino_ratio | -1.4921 |
| max_drawdown | 0.8213 |
| cagr | -0.5104 |
| net_avg_win | 47.5799 |
| net_avg_loss | -62.6482 |
| avg_hold_time_bars | 21.1417 |
| exposure | 0.6571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
