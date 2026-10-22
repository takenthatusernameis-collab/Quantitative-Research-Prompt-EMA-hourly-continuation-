# EMA Hourly Continuation — PYTH/USDT P21_50

**Symbol:** PYTH/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.5635 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -5.4894 |
| sortino_ratio | -2.4147 |
| max_drawdown | 0.9464 |
| cagr | -0.6860 |
| net_avg_win | 26.1872 |
| net_avg_loss | -42.7177 |
| avg_hold_time_bars | 4.5427 |
| exposure | 0.2009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
