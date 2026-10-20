# EMA Hourly Continuation — MTL/USDT P21_50

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.4532 |
| net_win_rate | 0.4192 |
| gross_profit_factor | 0.8585 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -8.0050 |
| sortino_ratio | -3.3651 |
| max_drawdown | 0.9853 |
| cagr | -0.8105 |
| net_avg_win | 22.0082 |
| net_avg_loss | -35.0477 |
| avg_hold_time_bars | 7.1164 |
| exposure | 0.2850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
