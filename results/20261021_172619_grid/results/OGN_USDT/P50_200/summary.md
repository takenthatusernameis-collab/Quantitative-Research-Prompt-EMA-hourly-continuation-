# EMA Hourly Continuation — OGN/USDT P50_200

**Symbol:** OGN/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.4762 |
| gross_profit_factor | 0.8847 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.0736 |
| sortino_ratio | -0.5378 |
| max_drawdown | 0.5095 |
| cagr | -0.2202 |
| net_avg_win | 64.1597 |
| net_avg_loss | -84.8054 |
| avg_hold_time_bars | 26.8185 |
| exposure | 0.4078 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
