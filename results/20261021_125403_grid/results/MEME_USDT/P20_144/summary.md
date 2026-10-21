# EMA Hourly Continuation — MEME/USDT P20_144

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.8230 |
| net_win_rate | 0.4973 |
| gross_profit_factor | 0.9857 |
| gross_win_rate | 0.4973 |
| sharpe_ratio | -1.1958 |
| sortino_ratio | -0.3262 |
| max_drawdown | 0.3932 |
| cagr | -0.1412 |
| net_avg_win | 81.6340 |
| net_avg_loss | -98.1032 |
| avg_hold_time_bars | 35.2995 |
| exposure | 0.5840 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
