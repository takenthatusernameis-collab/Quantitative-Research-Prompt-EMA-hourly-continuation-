# EMA Hourly Continuation — MEME/USDT P34_50

**Symbol:** MEME/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4776 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -2.5008 |
| sortino_ratio | -0.6324 |
| max_drawdown | 0.5717 |
| cagr | -0.2512 |
| net_avg_win | 67.5854 |
| net_avg_loss | -93.4596 |
| avg_hold_time_bars | 4.3622 |
| exposure | 0.0619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
