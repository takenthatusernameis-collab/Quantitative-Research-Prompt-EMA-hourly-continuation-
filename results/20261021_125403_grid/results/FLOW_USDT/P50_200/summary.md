# EMA Hourly Continuation — FLOW/USDT P50_200

**Symbol:** FLOW/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7266 |
| net_win_rate | 0.4739 |
| gross_profit_factor | 0.8928 |
| gross_win_rate | 0.4739 |
| sharpe_ratio | -1.7006 |
| sortino_ratio | -0.4237 |
| max_drawdown | 0.3928 |
| cagr | -0.1772 |
| net_avg_win | 70.9791 |
| net_avg_loss | -87.9740 |
| avg_hold_time_bars | 27.9314 |
| exposure | 0.3885 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
