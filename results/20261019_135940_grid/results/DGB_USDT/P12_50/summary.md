# EMA Hourly Continuation — DGB/USDT P12_50

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1193 |
| net_profit_factor | 0.4892 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8960 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -8.1442 |
| sortino_ratio | -3.9228 |
| max_drawdown | 0.9930 |
| cagr | -0.8602 |
| net_avg_win | 17.9078 |
| net_avg_loss | -29.3620 |
| avg_hold_time_bars | 6.5608 |
| exposure | 0.3558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
