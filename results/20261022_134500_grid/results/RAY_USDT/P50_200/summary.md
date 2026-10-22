# EMA Hourly Continuation — RAY/USDT P50_200

**Symbol:** RAY/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.6739 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9979 |
| gross_win_rate | 0.5026 |
| sharpe_ratio | -2.3464 |
| sortino_ratio | -0.6536 |
| max_drawdown | 0.5862 |
| cagr | -0.2682 |
| net_avg_win | 58.8076 |
| net_avg_loss | -82.9243 |
| avg_hold_time_bars | 19.4898 |
| exposure | 0.3473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
