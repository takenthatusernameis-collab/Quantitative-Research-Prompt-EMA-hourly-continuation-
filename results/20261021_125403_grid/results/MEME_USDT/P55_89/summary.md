# EMA Hourly Continuation — MEME/USDT P55_89

**Symbol:** MEME/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7860 |
| net_win_rate | 0.5150 |
| gross_profit_factor | 1.0566 |
| gross_win_rate | 0.5150 |
| sharpe_ratio | -1.3624 |
| sortino_ratio | -0.3584 |
| max_drawdown | 0.3434 |
| cagr | -0.1521 |
| net_avg_win | 72.4641 |
| net_avg_loss | -97.8813 |
| avg_hold_time_bars | 7.5749 |
| exposure | 0.1150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
