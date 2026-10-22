# EMA Hourly Continuation — TWT/USDT P12_200

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.6753 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9976 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -2.1902 |
| sortino_ratio | -0.6103 |
| max_drawdown | 0.5585 |
| cagr | -0.2479 |
| net_avg_win | 55.6576 |
| net_avg_loss | -81.5607 |
| avg_hold_time_bars | 42.8438 |
| exposure | 0.7478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
