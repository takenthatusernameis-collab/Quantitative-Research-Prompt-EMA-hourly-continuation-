# EMA Hourly Continuation — AEVO/USDT P55_100

**Symbol:** AEVO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6637 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.8749 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.4422 |
| sortino_ratio | -0.7098 |
| max_drawdown | 0.5722 |
| cagr | -0.2781 |
| net_avg_win | 55.8793 |
| net_avg_loss | -76.4648 |
| avg_hold_time_bars | 7.0745 |
| exposure | 0.1332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
