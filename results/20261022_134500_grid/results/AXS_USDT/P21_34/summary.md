# EMA Hourly Continuation — AXS/USDT P21_34

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.3204 |
| net_win_rate | 0.4134 |
| gross_profit_factor | 0.7996 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -10.9158 |
| sortino_ratio | -5.0948 |
| max_drawdown | 0.9986 |
| cagr | -0.9261 |
| net_avg_win | 10.6042 |
| net_avg_loss | -23.3242 |
| avg_hold_time_bars | 2.4777 |
| exposure | 0.1204 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
