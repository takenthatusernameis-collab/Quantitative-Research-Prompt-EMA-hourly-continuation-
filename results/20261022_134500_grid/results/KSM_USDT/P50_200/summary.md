# EMA Hourly Continuation — KSM/USDT P50_200

**Symbol:** KSM/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 381 |
| net_profit_factor | 0.6400 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9548 |
| gross_win_rate | 0.4856 |
| sharpe_ratio | -2.9791 |
| sortino_ratio | -0.8159 |
| max_drawdown | 0.6550 |
| cagr | -0.3271 |
| net_avg_win | 61.8940 |
| net_avg_loss | -87.5275 |
| avg_hold_time_bars | 21.8898 |
| exposure | 0.3791 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
