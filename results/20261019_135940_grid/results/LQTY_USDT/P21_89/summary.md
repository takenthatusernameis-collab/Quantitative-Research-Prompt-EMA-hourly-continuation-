# EMA Hourly Continuation — LQTY/USDT P21_89

**Symbol:** LQTY/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6222 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9020 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -3.9845 |
| sortino_ratio | -1.4764 |
| max_drawdown | 0.8322 |
| cagr | -0.4988 |
| net_avg_win | 42.5972 |
| net_avg_loss | -59.1817 |
| avg_hold_time_bars | 13.4360 |
| exposure | 0.4183 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
