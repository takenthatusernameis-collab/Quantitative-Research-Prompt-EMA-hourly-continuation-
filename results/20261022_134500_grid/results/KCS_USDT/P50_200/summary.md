# EMA Hourly Continuation — KCS/USDT P50_200

**Symbol:** KCS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.3832 |
| net_win_rate | 0.4133 |
| gross_profit_factor | 0.8743 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -5.7961 |
| sortino_ratio | -1.6111 |
| max_drawdown | 0.8765 |
| cagr | -0.5640 |
| net_avg_win | 33.5804 |
| net_avg_loss | -61.7241 |
| avg_hold_time_bars | 23.5663 |
| exposure | 0.4199 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
