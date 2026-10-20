# EMA Hourly Continuation — MEME/USDT P8_144

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.6705 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9092 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -2.7594 |
| sortino_ratio | -0.8390 |
| max_drawdown | 0.6530 |
| cagr | -0.3312 |
| net_avg_win | 58.2760 |
| net_avg_loss | -77.8059 |
| avg_hold_time_bars | 35.3638 |
| exposure | 0.7555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
