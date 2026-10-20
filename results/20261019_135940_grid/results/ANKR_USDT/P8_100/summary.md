# EMA Hourly Continuation — ANKR/USDT P8_100

**Symbol:** ANKR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6435 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9836 |
| gross_win_rate | 0.4931 |
| sharpe_ratio | -3.4712 |
| sortino_ratio | -1.1682 |
| max_drawdown | 0.7707 |
| cagr | -0.4337 |
| net_avg_win | 48.8265 |
| net_avg_loss | -71.7939 |
| avg_hold_time_bars | 27.0260 |
| exposure | 0.7100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
