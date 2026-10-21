# EMA Hourly Continuation — CGPT/USDT P8_144

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.9700 |
| net_win_rate | 0.5315 |
| gross_profit_factor | 1.1275 |
| gross_win_rate | 0.5315 |
| sharpe_ratio | -0.1305 |
| sortino_ratio | -0.0360 |
| max_drawdown | 0.1672 |
| cagr | -0.0227 |
| net_avg_win | 93.4010 |
| net_avg_loss | -109.2394 |
| avg_hold_time_bars | 45.2822 |
| exposure | 0.7513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
