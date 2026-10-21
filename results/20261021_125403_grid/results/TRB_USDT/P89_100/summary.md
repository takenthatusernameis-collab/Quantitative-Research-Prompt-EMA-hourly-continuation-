# EMA Hourly Continuation — TRB/USDT P89_100

**Symbol:** TRB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.6057 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -1.6445 |
| sortino_ratio | -0.2467 |
| max_drawdown | 0.2744 |
| cagr | -0.1068 |
| net_avg_win | 73.2524 |
| net_avg_loss | -108.4198 |
| avg_hold_time_bars | 4.7818 |
| exposure | 0.0238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
