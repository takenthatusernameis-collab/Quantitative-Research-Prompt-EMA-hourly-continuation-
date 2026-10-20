# EMA Hourly Continuation — EDU/USDT P8_26

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1519 |
| net_profit_factor | 0.4969 |
| net_win_rate | 0.4490 |
| gross_profit_factor | 0.8750 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -8.5148 |
| sortino_ratio | -4.6847 |
| max_drawdown | 0.9966 |
| cagr | -0.8935 |
| net_avg_win | 14.4285 |
| net_avg_loss | -23.6619 |
| avg_hold_time_bars | 4.5510 |
| exposure | 0.3128 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
