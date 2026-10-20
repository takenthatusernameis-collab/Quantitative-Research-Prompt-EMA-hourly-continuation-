# EMA Hourly Continuation — UMA/USDT P20_50

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.4764 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.8664 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -6.9591 |
| sortino_ratio | -3.0532 |
| max_drawdown | 0.9759 |
| cagr | -0.7706 |
| net_avg_win | 20.3021 |
| net_avg_loss | -35.4072 |
| avg_hold_time_bars | 5.7850 |
| exposure | 0.2532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
