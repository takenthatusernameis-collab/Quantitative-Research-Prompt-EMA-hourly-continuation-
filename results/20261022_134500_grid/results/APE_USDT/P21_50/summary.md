# EMA Hourly Continuation — APE/USDT P21_50

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1018 |
| net_profit_factor | 0.4983 |
| net_win_rate | 0.4695 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -6.8214 |
| sortino_ratio | -3.0702 |
| max_drawdown | 0.9777 |
| cagr | -0.7750 |
| net_avg_win | 20.2911 |
| net_avg_loss | -36.0427 |
| avg_hold_time_bars | 3.9627 |
| exposure | 0.1834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
