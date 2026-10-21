# EMA Hourly Continuation — HTX/USDT P12_26

**Symbol:** HTX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.3533 |
| net_win_rate | 0.3527 |
| gross_profit_factor | 0.6429 |
| gross_win_rate | 0.3564 |
| sharpe_ratio | -8.6964 |
| sortino_ratio | -2.9800 |
| max_drawdown | 0.9725 |
| cagr | -0.7596 |
| net_avg_win | 27.3849 |
| net_avg_loss | -42.2419 |
| avg_hold_time_bars | 6.4127 |
| exposure | 0.1596 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
