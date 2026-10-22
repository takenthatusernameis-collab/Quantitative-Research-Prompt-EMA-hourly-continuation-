# EMA Hourly Continuation — ETC/USDT P12_144

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5751 |
| net_win_rate | 0.4701 |
| gross_profit_factor | 0.9530 |
| gross_win_rate | 0.4855 |
| sharpe_ratio | -4.0300 |
| sortino_ratio | -1.2888 |
| max_drawdown | 0.8091 |
| cagr | -0.4628 |
| net_avg_win | 43.8261 |
| net_avg_loss | -67.6103 |
| avg_hold_time_bars | 27.3044 |
| exposure | 0.6441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
