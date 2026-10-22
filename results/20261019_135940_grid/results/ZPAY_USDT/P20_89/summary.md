# EMA Hourly Continuation — ZPAY/USDT P20_89

**Symbol:** ZPAY/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 574 |
| net_profit_factor | 0.4580 |
| net_win_rate | 0.3432 |
| gross_profit_factor | 0.5990 |
| gross_win_rate | 0.3449 |
| sharpe_ratio | -6.4056 |
| sortino_ratio | -2.1403 |
| max_drawdown | 0.9250 |
| cagr | -0.6347 |
| net_avg_win | 39.5094 |
| net_avg_loss | -45.0789 |
| avg_hold_time_bars | 18.8815 |
| exposure | 0.4904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
