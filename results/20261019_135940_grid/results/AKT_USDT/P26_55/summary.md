# EMA Hourly Continuation — AKT/USDT P26_55

**Symbol:** AKT/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 898 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -5.7447 |
| sortino_ratio | -2.4335 |
| max_drawdown | 0.9502 |
| cagr | -0.6900 |
| net_avg_win | 26.4388 |
| net_avg_loss | -44.0792 |
| avg_hold_time_bars | 4.2506 |
| exposure | 0.1735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
