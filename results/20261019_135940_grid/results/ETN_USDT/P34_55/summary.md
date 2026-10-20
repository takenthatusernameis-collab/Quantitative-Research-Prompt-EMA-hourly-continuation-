# EMA Hourly Continuation — ETN/USDT P34_55

**Symbol:** ETN/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 837 |
| net_profit_factor | 0.2609 |
| net_win_rate | 0.3321 |
| gross_profit_factor | 0.4652 |
| gross_win_rate | 0.3536 |
| sharpe_ratio | -12.4380 |
| sortino_ratio | -5.6270 |
| max_drawdown | 0.9977 |
| cagr | -0.9437 |
| net_avg_win | 12.6682 |
| net_avg_loss | -24.1469 |
| avg_hold_time_bars | 3.1935 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
