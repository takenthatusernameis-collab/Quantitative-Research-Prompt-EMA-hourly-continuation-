# EMA Hourly Continuation — CHR/USDT P26_200

**Symbol:** CHR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 284 |
| net_profit_factor | 0.8467 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9961 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.8417 |
| sortino_ratio | -0.2026 |
| max_drawdown | 0.2501 |
| cagr | -0.0908 |
| net_avg_win | 83.0624 |
| net_avg_loss | -98.0963 |
| avg_hold_time_bars | 48.5599 |
| exposure | 0.6241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
