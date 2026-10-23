# EMA Hourly Continuation — FLOW/USDT P34_100

**Symbol:** FLOW/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.5239 |
| net_win_rate | 0.4404 |
| gross_profit_factor | 0.8567 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -5.4224 |
| sortino_ratio | -1.9997 |
| max_drawdown | 0.9155 |
| cagr | -0.6204 |
| net_avg_win | 33.1245 |
| net_avg_loss | -49.7622 |
| avg_hold_time_bars | 8.3067 |
| exposure | 0.2598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
