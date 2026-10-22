# EMA Hourly Continuation — NEAR/USDT P12_144

**Symbol:** NEAR/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.7448 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 1.0056 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.9878 |
| sortino_ratio | -0.6023 |
| max_drawdown | 0.5379 |
| cagr | -0.2442 |
| net_avg_win | 66.3923 |
| net_avg_loss | -85.2936 |
| avg_hold_time_bars | 32.7423 |
| exposure | 0.6757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
