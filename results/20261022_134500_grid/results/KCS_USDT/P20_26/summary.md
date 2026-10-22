# EMA Hourly Continuation — KCS/USDT P20_26

**Symbol:** KCS/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1179 |
| net_profit_factor | 0.0486 |
| net_win_rate | 0.1841 |
| gross_profit_factor | 0.5009 |
| gross_win_rate | 0.3189 |
| sharpe_ratio | -22.0685 |
| sortino_ratio | -12.8500 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 2.3522 |
| net_avg_loss | -10.9256 |
| avg_hold_time_bars | 2.2994 |
| exposure | 0.1232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
