# EMA Hourly Continuation — MEME/USDT P50_89

**Symbol:** MEME/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5506 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8882 |
| gross_win_rate | 0.4699 |
| sharpe_ratio | -5.0288 |
| sortino_ratio | -1.8580 |
| max_drawdown | 0.8963 |
| cagr | -0.5896 |
| net_avg_win | 34.7372 |
| net_avg_loss | -54.3005 |
| avg_hold_time_bars | 5.2144 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
