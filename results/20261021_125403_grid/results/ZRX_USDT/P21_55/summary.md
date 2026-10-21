# EMA Hourly Continuation — ZRX/USDT P21_55

**Symbol:** ZRX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6745 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -3.3833 |
| sortino_ratio | -1.1910 |
| max_drawdown | 0.7534 |
| cagr | -0.4212 |
| net_avg_win | 53.3468 |
| net_avg_loss | -72.8191 |
| avg_hold_time_bars | 8.4413 |
| exposure | 0.2321 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
