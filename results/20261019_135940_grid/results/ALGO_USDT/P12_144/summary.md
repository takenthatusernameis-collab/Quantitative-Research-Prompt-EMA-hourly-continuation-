# EMA Hourly Continuation — ALGO/USDT P12_144

**Symbol:** ALGO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7544 |
| net_win_rate | 0.5174 |
| gross_profit_factor | 1.0490 |
| gross_win_rate | 0.5199 |
| sharpe_ratio | -1.5751 |
| sortino_ratio | -0.4440 |
| max_drawdown | 0.4624 |
| cagr | -0.1926 |
| net_avg_win | 61.3871 |
| net_avg_loss | -87.2449 |
| avg_hold_time_bars | 39.5373 |
| exposure | 0.7225 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
