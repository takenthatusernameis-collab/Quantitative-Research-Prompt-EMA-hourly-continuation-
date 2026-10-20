# EMA Hourly Continuation — ZETA/USDT P12_200

**Symbol:** ZETA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.7314 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.6788 |
| sortino_ratio | -0.4033 |
| max_drawdown | 0.4666 |
| cagr | -0.1751 |
| net_avg_win | 71.7302 |
| net_avg_loss | -97.4075 |
| avg_hold_time_bars | 59.1706 |
| exposure | 0.7845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
