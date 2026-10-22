# EMA Hourly Continuation — RUNE/USDT P34_50

**Symbol:** RUNE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.4313 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9324 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -8.3934 |
| sortino_ratio | -3.5639 |
| max_drawdown | 0.9897 |
| cagr | -0.8374 |
| net_avg_win | 18.0365 |
| net_avg_loss | -35.7263 |
| avg_hold_time_bars | 2.7519 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
