# EMA Hourly Continuation — UMA/USDT P34_100

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.6025 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9831 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -4.1933 |
| sortino_ratio | -1.5149 |
| max_drawdown | 0.8492 |
| cagr | -0.5148 |
| net_avg_win | 40.6817 |
| net_avg_loss | -61.4168 |
| avg_hold_time_bars | 9.4580 |
| exposure | 0.2816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
