# EMA Hourly Continuation — APE/USDT P21_50

**Symbol:** APE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 470 |
| net_profit_factor | 0.7151 |
| net_win_rate | 0.4809 |
| gross_profit_factor | 0.9520 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -2.4935 |
| sortino_ratio | -0.7728 |
| max_drawdown | 0.6073 |
| cagr | -0.2984 |
| net_avg_win | 65.4575 |
| net_avg_loss | -84.7841 |
| avg_hold_time_bars | 6.6021 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
