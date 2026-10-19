# EMA Hourly Continuation — FIL/USDT P8_55

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1012 |
| net_profit_factor | 0.5569 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.9534 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -6.1249 |
| sortino_ratio | -2.7419 |
| max_drawdown | 0.9656 |
| cagr | -0.7348 |
| net_avg_win | 25.6735 |
| net_avg_loss | -40.2983 |
| avg_hold_time_bars | 11.0405 |
| exposure | 0.5079 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
