# EMA Hourly Continuation — AURORA/USDT P50_100

**Symbol:** AURORA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.4956 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.9054 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -5.7518 |
| sortino_ratio | -1.8867 |
| max_drawdown | 0.9135 |
| cagr | -0.6170 |
| net_avg_win | 36.5022 |
| net_avg_loss | -59.1641 |
| avg_hold_time_bars | 6.7636 |
| exposure | 0.1691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
