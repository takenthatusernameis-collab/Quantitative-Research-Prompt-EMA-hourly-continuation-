# EMA Hourly Continuation — MLK/USDT P8_50

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1413 |
| net_profit_factor | 0.3105 |
| net_win_rate | 0.3043 |
| gross_profit_factor | 0.6150 |
| gross_win_rate | 0.3171 |
| sharpe_ratio | -15.2201 |
| sortino_ratio | -8.1249 |
| max_drawdown | 1.0000 |
| cagr | -0.9842 |
| net_avg_win | 10.4719 |
| net_avg_loss | -14.7534 |
| avg_hold_time_bars | 6.7700 |
| exposure | 0.4329 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
