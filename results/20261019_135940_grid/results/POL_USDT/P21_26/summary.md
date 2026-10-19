# EMA Hourly Continuation — POL/USDT P21_26

**Symbol:** POL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1262 |
| net_profit_factor | 0.1700 |
| net_win_rate | 0.3352 |
| gross_profit_factor | 0.6535 |
| gross_win_rate | 0.3914 |
| sharpe_ratio | -16.3688 |
| sortino_ratio | -8.5670 |
| max_drawdown | 1.0000 |
| cagr | -0.9909 |
| net_avg_win | 4.8407 |
| net_avg_loss | -14.3594 |
| avg_hold_time_bars | 1.8827 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
