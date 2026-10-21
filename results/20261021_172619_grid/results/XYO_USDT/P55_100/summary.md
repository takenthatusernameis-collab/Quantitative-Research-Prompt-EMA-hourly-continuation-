# EMA Hourly Continuation — XYO/USDT P55_100

**Symbol:** XYO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.5950 |
| net_win_rate | 0.4504 |
| gross_profit_factor | 0.8492 |
| gross_win_rate | 0.4504 |
| sharpe_ratio | -3.2865 |
| sortino_ratio | -0.8796 |
| max_drawdown | 0.6449 |
| cagr | -0.3342 |
| net_avg_win | 59.2781 |
| net_avg_loss | -81.6533 |
| avg_hold_time_bars | 9.3144 |
| exposure | 0.1488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
