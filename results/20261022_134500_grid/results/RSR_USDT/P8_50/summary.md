# EMA Hourly Continuation — RSR/USDT P8_50

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1117 |
| net_profit_factor | 0.6178 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -5.2437 |
| sortino_ratio | -2.4656 |
| max_drawdown | 0.9493 |
| cagr | -0.6922 |
| net_avg_win | 28.7577 |
| net_avg_loss | -42.4818 |
| avg_hold_time_bars | 8.9982 |
| exposure | 0.4569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
