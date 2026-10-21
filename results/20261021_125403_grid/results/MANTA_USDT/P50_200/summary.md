# EMA Hourly Continuation — MANTA/USDT P50_200

**Symbol:** MANTA/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 272 |
| net_profit_factor | 0.7980 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9519 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -1.1571 |
| sortino_ratio | -0.2725 |
| max_drawdown | 0.3024 |
| cagr | -0.1187 |
| net_avg_win | 80.7797 |
| net_avg_loss | -96.8595 |
| avg_hold_time_bars | 38.2463 |
| exposure | 0.4729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
