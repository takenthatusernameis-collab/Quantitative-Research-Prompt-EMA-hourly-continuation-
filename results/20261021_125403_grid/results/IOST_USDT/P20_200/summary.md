# EMA Hourly Continuation — IOST/USDT P20_200

**Symbol:** IOST/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.9616 |
| net_win_rate | 0.5505 |
| gross_profit_factor | 1.2092 |
| gross_win_rate | 0.5505 |
| sharpe_ratio | -0.1611 |
| sortino_ratio | -0.0422 |
| max_drawdown | 0.1782 |
| cagr | -0.0246 |
| net_avg_win | 84.4948 |
| net_avg_loss | -107.5908 |
| avg_hold_time_bars | 42.4159 |
| exposure | 0.6305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
