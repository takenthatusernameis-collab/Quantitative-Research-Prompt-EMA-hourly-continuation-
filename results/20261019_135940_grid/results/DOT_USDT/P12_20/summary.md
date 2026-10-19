# EMA Hourly Continuation — DOT/USDT P12_20

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1513 |
| net_profit_factor | 0.2210 |
| net_win_rate | 0.4052 |
| gross_profit_factor | 0.8439 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -14.7625 |
| sortino_ratio | -8.2403 |
| max_drawdown | 1.0000 |
| cagr | -0.9873 |
| net_avg_win | 4.6282 |
| net_avg_loss | -14.2632 |
| avg_hold_time_bars | 2.0165 |
| exposure | 0.1387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
