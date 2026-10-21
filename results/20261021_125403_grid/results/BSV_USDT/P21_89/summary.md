# EMA Hourly Continuation — BSV/USDT P21_89

**Symbol:** BSV/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8563 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.2719 |
| sortino_ratio | -1.0600 |
| max_drawdown | 0.7167 |
| cagr | -0.3845 |
| net_avg_win | 53.9948 |
| net_avg_loss | -70.8024 |
| avg_hold_time_bars | 15.4817 |
| exposure | 0.3652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
