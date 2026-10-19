# EMA Hourly Continuation — TWT/USDT P20_144

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.5873 |
| net_win_rate | 0.4819 |
| gross_profit_factor | 0.9329 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -3.7321 |
| sortino_ratio | -1.2312 |
| max_drawdown | 0.7940 |
| cagr | -0.4490 |
| net_avg_win | 41.5137 |
| net_avg_loss | -65.7470 |
| avg_hold_time_bars | 21.0000 |
| exposure | 0.5269 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
