# EMA Hourly Continuation — STRAX/USDT P8_21

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1497 |
| net_profit_factor | 0.3734 |
| net_win_rate | 0.3781 |
| gross_profit_factor | 0.7336 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -13.4457 |
| sortino_ratio | -7.3790 |
| max_drawdown | 0.9999 |
| cagr | -0.9771 |
| net_avg_win | 10.5288 |
| net_avg_loss | -17.1412 |
| avg_hold_time_bars | 4.0929 |
| exposure | 0.2801 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
