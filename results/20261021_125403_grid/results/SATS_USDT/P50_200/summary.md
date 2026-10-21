# EMA Hourly Continuation — SATS/USDT P50_200

**Symbol:** SATS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.7061 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -1.8411 |
| sortino_ratio | -0.4488 |
| max_drawdown | 0.4268 |
| cagr | -0.1863 |
| net_avg_win | 71.1232 |
| net_avg_loss | -86.7924 |
| avg_hold_time_bars | 25.8547 |
| exposure | 0.3463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
