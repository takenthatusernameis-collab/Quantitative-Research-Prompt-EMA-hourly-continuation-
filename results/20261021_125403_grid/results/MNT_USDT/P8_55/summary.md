# EMA Hourly Continuation — MNT/USDT P8_55

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.7419 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 0.9968 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -2.1628 |
| sortino_ratio | -0.7983 |
| max_drawdown | 0.6075 |
| cagr | -0.3083 |
| net_avg_win | 51.6390 |
| net_avg_loss | -71.5216 |
| avg_hold_time_bars | 16.6335 |
| exposure | 0.5013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
