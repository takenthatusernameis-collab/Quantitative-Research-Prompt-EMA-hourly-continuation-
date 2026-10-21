# EMA Hourly Continuation — RAY/USDT P12_200

**Symbol:** RAY/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7810 |
| net_win_rate | 0.4756 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4756 |
| sharpe_ratio | -1.4465 |
| sortino_ratio | -0.3842 |
| max_drawdown | 0.4039 |
| cagr | -0.1634 |
| net_avg_win | 77.5656 |
| net_avg_loss | -90.0928 |
| avg_hold_time_bars | 43.1977 |
| exposure | 0.6853 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
