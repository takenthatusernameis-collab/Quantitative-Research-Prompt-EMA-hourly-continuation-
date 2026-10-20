# EMA Hourly Continuation — UMA/USDT P12_144

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 557 |
| net_profit_factor | 0.6395 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -2.9653 |
| sortino_ratio | -0.9878 |
| max_drawdown | 0.7017 |
| cagr | -0.3712 |
| net_avg_win | 45.2085 |
| net_avg_loss | -66.5068 |
| avg_hold_time_bars | 24.1436 |
| exposure | 0.6113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
