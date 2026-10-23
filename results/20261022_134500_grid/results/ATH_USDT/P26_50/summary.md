# EMA Hourly Continuation — ATH/USDT P26_50

**Symbol:** ATH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.4376 |
| net_win_rate | 0.4519 |
| gross_profit_factor | 0.7898 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -7.1630 |
| sortino_ratio | -3.1189 |
| max_drawdown | 0.9743 |
| cagr | -0.7844 |
| net_avg_win | 18.7384 |
| net_avg_loss | -35.3073 |
| avg_hold_time_bars | 3.4340 |
| exposure | 0.1488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
