# EMA Hourly Continuation — CELR/USDT P26_50

**Symbol:** CELR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.4772 |
| net_win_rate | 0.4487 |
| gross_profit_factor | 0.8784 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -6.9916 |
| sortino_ratio | -3.0391 |
| max_drawdown | 0.9747 |
| cagr | -0.7672 |
| net_avg_win | 20.9841 |
| net_avg_loss | -35.7852 |
| avg_hold_time_bars | 4.6444 |
| exposure | 0.1986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
