# EMA Hourly Continuation — FLUX/USDT P20_200

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.8563 |
| net_win_rate | 0.5048 |
| gross_profit_factor | 1.0203 |
| gross_win_rate | 0.5048 |
| sharpe_ratio | -0.8399 |
| sortino_ratio | -0.2122 |
| max_drawdown | 0.2771 |
| cagr | -0.0952 |
| net_avg_win | 84.2706 |
| net_avg_loss | -100.3315 |
| avg_hold_time_bars | 44.6945 |
| exposure | 0.6318 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
