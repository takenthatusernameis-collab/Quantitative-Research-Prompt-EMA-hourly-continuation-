# EMA Hourly Continuation — BONK/USDT P8_34

**Symbol:** BONK/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1406 |
| net_profit_factor | 0.5865 |
| net_win_rate | 0.4531 |
| gross_profit_factor | 0.9250 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -7.5614 |
| sortino_ratio | -3.9749 |
| max_drawdown | 0.9927 |
| cagr | -0.8567 |
| net_avg_win | 22.0961 |
| net_avg_loss | -31.2083 |
| avg_hold_time_bars | 4.9943 |
| exposure | 0.3192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
