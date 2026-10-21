# EMA Hourly Continuation — SHIB/USDT P8_34

**Symbol:** SHIB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 675 |
| net_profit_factor | 0.7548 |
| net_win_rate | 0.5096 |
| gross_profit_factor | 1.0341 |
| gross_win_rate | 0.5096 |
| sharpe_ratio | -2.3247 |
| sortino_ratio | -0.8686 |
| max_drawdown | 0.6383 |
| cagr | -0.3281 |
| net_avg_win | 56.5314 |
| net_avg_loss | -77.8351 |
| avg_hold_time_bars | 8.4089 |
| exposure | 0.2580 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
