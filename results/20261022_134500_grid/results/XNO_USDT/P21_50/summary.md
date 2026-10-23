# EMA Hourly Continuation — XNO/USDT P21_50

**Symbol:** XNO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.4524 |
| net_win_rate | 0.3939 |
| gross_profit_factor | 0.8296 |
| gross_win_rate | 0.4096 |
| sharpe_ratio | -10.2603 |
| sortino_ratio | -4.9276 |
| max_drawdown | 0.9980 |
| cagr | -0.9129 |
| net_avg_win | 18.1950 |
| net_avg_loss | -26.1414 |
| avg_hold_time_bars | 3.8904 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
