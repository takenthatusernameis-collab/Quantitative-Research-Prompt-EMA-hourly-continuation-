# EMA Hourly Continuation — VET/USDT P8_21

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.6877 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 0.9947 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -2.6740 |
| sortino_ratio | -0.8935 |
| max_drawdown | 0.6482 |
| cagr | -0.3347 |
| net_avg_win | 52.0458 |
| net_avg_loss | -76.2464 |
| avg_hold_time_bars | 5.3352 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
