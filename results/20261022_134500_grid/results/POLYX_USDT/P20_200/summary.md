# EMA Hourly Continuation — POLYX/USDT P20_200

**Symbol:** POLYX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 394 |
| net_profit_factor | 0.7157 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0209 |
| gross_win_rate | 0.5127 |
| sharpe_ratio | -1.9474 |
| sortino_ratio | -0.5444 |
| max_drawdown | 0.5174 |
| cagr | -0.2279 |
| net_avg_win | 61.0466 |
| net_avg_loss | -85.2961 |
| avg_hold_time_bars | 34.8832 |
| exposure | 0.6247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
