# EMA Hourly Continuation — UNI/USDT P8_144

**Symbol:** UNI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6115 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4574 |
| sharpe_ratio | -3.7645 |
| sortino_ratio | -1.1776 |
| max_drawdown | 0.7691 |
| cagr | -0.4378 |
| net_avg_win | 52.5412 |
| net_avg_loss | -71.2933 |
| avg_hold_time_bars | 31.8752 |
| exposure | 0.7317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
