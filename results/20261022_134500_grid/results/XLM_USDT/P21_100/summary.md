# EMA Hourly Continuation — XLM/USDT P21_100

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.4796 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9524 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -4.7639 |
| sortino_ratio | -1.6936 |
| max_drawdown | 0.8862 |
| cagr | -0.5677 |
| net_avg_win | 25.9456 |
| net_avg_loss | -50.5329 |
| avg_hold_time_bars | 14.7276 |
| exposure | 0.4325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
