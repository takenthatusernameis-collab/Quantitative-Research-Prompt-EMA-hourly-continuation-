# EMA Hourly Continuation — WIF/USDT P20_100

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.8450 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 0.9863 |
| gross_win_rate | 0.4989 |
| sharpe_ratio | -1.0962 |
| sortino_ratio | -0.3286 |
| max_drawdown | 0.3912 |
| cagr | -0.1431 |
| net_avg_win | 80.0045 |
| net_avg_loss | -94.2549 |
| avg_hold_time_bars | 19.5376 |
| exposure | 0.3899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
