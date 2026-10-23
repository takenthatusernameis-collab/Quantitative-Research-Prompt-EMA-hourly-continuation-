# EMA Hourly Continuation — IO/USDT P20_55

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.5799 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8608 |
| gross_win_rate | 0.4661 |
| sharpe_ratio | -5.6216 |
| sortino_ratio | -2.4495 |
| max_drawdown | 0.9382 |
| cagr | -0.6922 |
| net_avg_win | 31.4292 |
| net_avg_loss | -45.6596 |
| avg_hold_time_bars | 5.3552 |
| exposure | 0.2336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
