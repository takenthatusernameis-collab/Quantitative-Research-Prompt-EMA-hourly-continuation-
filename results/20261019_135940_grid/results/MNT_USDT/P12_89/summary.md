# EMA Hourly Continuation — MNT/USDT P12_89

**Symbol:** MNT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.4476 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.7871 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -5.6744 |
| sortino_ratio | -2.0225 |
| max_drawdown | 0.9228 |
| cagr | -0.6358 |
| net_avg_win | 26.1765 |
| net_avg_loss | -45.5438 |
| avg_hold_time_bars | 19.2320 |
| exposure | 0.5691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
