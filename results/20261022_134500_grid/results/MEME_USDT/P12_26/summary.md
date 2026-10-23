# EMA Hourly Continuation — MEME/USDT P12_26

**Symbol:** MEME/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1409 |
| net_profit_factor | 0.4625 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.9073 |
| gross_win_rate | 0.4436 |
| sharpe_ratio | -10.0845 |
| sortino_ratio | -5.3308 |
| max_drawdown | 0.9987 |
| cagr | -0.9281 |
| net_avg_win | 14.2506 |
| net_avg_loss | -23.0517 |
| avg_hold_time_bars | 3.1320 |
| exposure | 0.2006 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
