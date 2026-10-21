# EMA Hourly Continuation — BNB/USDT P12_100

**Symbol:** BNB/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6190 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -3.3459 |
| sortino_ratio | -1.0038 |
| max_drawdown | 0.6967 |
| cagr | -0.3703 |
| net_avg_win | 52.6607 |
| net_avg_loss | -79.4464 |
| avg_hold_time_bars | 28.1913 |
| exposure | 0.5625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
