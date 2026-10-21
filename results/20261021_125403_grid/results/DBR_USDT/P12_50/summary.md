# EMA Hourly Continuation — DBR/USDT P12_50

**Symbol:** DBR/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6226 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8919 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -3.8901 |
| sortino_ratio | -1.3366 |
| max_drawdown | 0.7314 |
| cagr | -0.4606 |
| net_avg_win | 54.5149 |
| net_avg_loss | -74.7015 |
| avg_hold_time_bars | 12.2591 |
| exposure | 0.3256 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
