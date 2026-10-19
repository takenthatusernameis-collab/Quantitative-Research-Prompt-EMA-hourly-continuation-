# EMA Hourly Continuation — TWT/USDT P20_26

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1300 |
| net_profit_factor | 0.1941 |
| net_win_rate | 0.3423 |
| gross_profit_factor | 0.7514 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -16.2925 |
| sortino_ratio | -8.7258 |
| max_drawdown | 1.0000 |
| cagr | -0.9904 |
| net_avg_win | 5.4119 |
| net_avg_loss | -14.5125 |
| avg_hold_time_bars | 2.0415 |
| exposure | 0.1206 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
