# EMA Hourly Continuation — METIS/USDT P34_200

**Symbol:** METIS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6032 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8152 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -2.9785 |
| sortino_ratio | -0.8180 |
| max_drawdown | 0.6207 |
| cagr | -0.3202 |
| net_avg_win | 55.1887 |
| net_avg_loss | -74.4965 |
| avg_hold_time_bars | 30.7953 |
| exposure | 0.5333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
