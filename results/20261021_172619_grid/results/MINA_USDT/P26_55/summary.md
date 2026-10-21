# EMA Hourly Continuation — MINA/USDT P26_55

**Symbol:** MINA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 495 |
| net_profit_factor | 0.7517 |
| net_win_rate | 0.5091 |
| gross_profit_factor | 1.0385 |
| gross_win_rate | 0.5091 |
| sharpe_ratio | -2.0340 |
| sortino_ratio | -0.6504 |
| max_drawdown | 0.5685 |
| cagr | -0.2578 |
| net_avg_win | 63.3091 |
| net_avg_loss | -87.3418 |
| avg_hold_time_bars | 7.6525 |
| exposure | 0.1722 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
