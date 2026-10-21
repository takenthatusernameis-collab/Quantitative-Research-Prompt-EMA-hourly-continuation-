# EMA Hourly Continuation — UMA/USDT P20_200

**Symbol:** UMA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.8351 |
| net_win_rate | 0.5125 |
| gross_profit_factor | 1.0244 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -0.9546 |
| sortino_ratio | -0.2600 |
| max_drawdown | 0.2785 |
| cagr | -0.1146 |
| net_avg_win | 72.0759 |
| net_avg_loss | -90.7229 |
| avg_hold_time_bars | 35.8449 |
| exposure | 0.5882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
