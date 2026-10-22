# EMA Hourly Continuation — RENDER/USDT P20_200

**Symbol:** RENDER/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8846 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1358 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -0.6525 |
| sortino_ratio | -0.1751 |
| max_drawdown | 0.2490 |
| cagr | -0.0818 |
| net_avg_win | 79.2615 |
| net_avg_loss | -103.5827 |
| avg_hold_time_bars | 40.0822 |
| exposure | 0.6431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
