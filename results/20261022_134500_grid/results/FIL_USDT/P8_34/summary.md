# EMA Hourly Continuation — FIL/USDT P8_34

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1369 |
| net_profit_factor | 0.4500 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.9288 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -9.2484 |
| sortino_ratio | -4.8006 |
| max_drawdown | 0.9976 |
| cagr | -0.9091 |
| net_avg_win | 13.4911 |
| net_avg_loss | -23.7406 |
| avg_hold_time_bars | 5.6764 |
| exposure | 0.3532 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
