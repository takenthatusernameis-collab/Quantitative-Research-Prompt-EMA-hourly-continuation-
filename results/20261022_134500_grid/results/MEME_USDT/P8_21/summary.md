# EMA Hourly Continuation — MEME/USDT P8_21

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1651 |
| net_profit_factor | 0.4459 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 0.9060 |
| gross_win_rate | 0.4518 |
| sharpe_ratio | -10.7006 |
| sortino_ratio | -6.1208 |
| max_drawdown | 0.9995 |
| cagr | -0.9518 |
| net_avg_win | 11.1848 |
| net_avg_loss | -19.3529 |
| avg_hold_time_bars | 3.0000 |
| exposure | 0.2251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
