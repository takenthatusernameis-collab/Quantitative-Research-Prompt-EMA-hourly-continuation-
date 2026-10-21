# EMA Hourly Continuation — MTL/USDT P21_89

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.6430 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8663 |
| gross_win_rate | 0.4599 |
| sharpe_ratio | -3.1637 |
| sortino_ratio | -0.9647 |
| max_drawdown | 0.6848 |
| cagr | -0.3591 |
| net_avg_win | 57.3118 |
| net_avg_loss | -75.8822 |
| avg_hold_time_bars | 21.7831 |
| exposure | 0.4544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
