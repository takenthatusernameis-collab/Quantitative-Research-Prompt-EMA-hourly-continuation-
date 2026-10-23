# EMA Hourly Continuation — FLUX/USDT P34_50

**Symbol:** FLUX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 934 |
| net_profit_factor | 0.3385 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8322 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -9.0977 |
| sortino_ratio | -3.9446 |
| max_drawdown | 0.9937 |
| cagr | -0.8649 |
| net_avg_win | 12.3986 |
| net_avg_loss | -28.6600 |
| avg_hold_time_bars | 2.3458 |
| exposure | 0.0996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
