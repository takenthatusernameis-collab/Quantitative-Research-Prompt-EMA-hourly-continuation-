# EMA Hourly Continuation — FLOKI/USDT P55_89

**Symbol:** FLOKI/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9669 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.7729 |
| sortino_ratio | -0.4611 |
| max_drawdown | 0.4376 |
| cagr | -0.1905 |
| net_avg_win | 68.7724 |
| net_avg_loss | -91.7837 |
| avg_hold_time_bars | 7.1091 |
| exposure | 0.1066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
