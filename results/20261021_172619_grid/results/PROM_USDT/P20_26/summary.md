# EMA Hourly Continuation — PROM/USDT P20_26

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.4034 |
| net_win_rate | 0.4158 |
| gross_profit_factor | 0.6732 |
| gross_win_rate | 0.4191 |
| sharpe_ratio | -4.4001 |
| sortino_ratio | -1.0943 |
| max_drawdown | 0.7429 |
| cagr | -0.4053 |
| net_avg_win | 39.1097 |
| net_avg_loss | -69.0169 |
| avg_hold_time_bars | 4.5413 |
| exposure | 0.0625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
