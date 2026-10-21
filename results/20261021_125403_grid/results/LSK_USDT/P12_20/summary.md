# EMA Hourly Continuation — LSK/USDT P12_20

**Symbol:** LSK/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6585 |
| net_win_rate | 0.5029 |
| gross_profit_factor | 1.0973 |
| gross_win_rate | 0.5067 |
| sharpe_ratio | -3.3841 |
| sortino_ratio | -1.1108 |
| max_drawdown | 0.7470 |
| cagr | -0.3994 |
| net_avg_win | 53.3480 |
| net_avg_loss | -81.9544 |
| avg_hold_time_bars | 5.3353 |
| exposure | 0.1259 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
