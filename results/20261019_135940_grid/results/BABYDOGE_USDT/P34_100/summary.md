# EMA Hourly Continuation — BABYDOGE/USDT P34_100

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 45 |
| net_profit_factor | 0.9534 |
| net_win_rate | 0.5111 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5111 |
| sharpe_ratio | -0.0792 |
| sortino_ratio | -0.0076 |
| max_drawdown | 0.0635 |
| cagr | -0.0042 |
| net_avg_win | 94.6855 |
| net_avg_loss | -103.8314 |
| avg_hold_time_bars | 23.0000 |
| exposure | 0.0468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
