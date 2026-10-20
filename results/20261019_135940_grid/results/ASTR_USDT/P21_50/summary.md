# EMA Hourly Continuation — ASTR/USDT P21_50

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 893 |
| net_profit_factor | 0.5058 |
| net_win_rate | 0.4748 |
| gross_profit_factor | 0.9649 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -6.4283 |
| sortino_ratio | -2.6986 |
| max_drawdown | 0.9657 |
| cagr | -0.7340 |
| net_avg_win | 23.2824 |
| net_avg_loss | -41.6149 |
| avg_hold_time_bars | 5.4267 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
