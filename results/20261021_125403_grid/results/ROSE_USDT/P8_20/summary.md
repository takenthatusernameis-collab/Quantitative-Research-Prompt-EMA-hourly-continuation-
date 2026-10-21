# EMA Hourly Continuation — ROSE/USDT P8_20

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7871 |
| net_win_rate | 0.5118 |
| gross_profit_factor | 1.0576 |
| gross_win_rate | 0.5118 |
| sharpe_ratio | -1.8828 |
| sortino_ratio | -0.6358 |
| max_drawdown | 0.5555 |
| cagr | -0.2532 |
| net_avg_win | 68.1002 |
| net_avg_loss | -90.7053 |
| avg_hold_time_bars | 5.3285 |
| exposure | 0.1335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
