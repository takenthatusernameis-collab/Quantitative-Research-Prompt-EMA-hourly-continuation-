# EMA Hourly Continuation — FIL/USDT P20_100

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4535 |
| gross_profit_factor | 0.8337 |
| gross_win_rate | 0.4535 |
| sharpe_ratio | -2.8058 |
| sortino_ratio | -0.8463 |
| max_drawdown | 0.6426 |
| cagr | -0.3223 |
| net_avg_win | 59.3021 |
| net_avg_loss | -74.4659 |
| avg_hold_time_bars | 18.3363 |
| exposure | 0.3767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
