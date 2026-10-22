# EMA Hourly Continuation — MANTA/USDT P55_200

**Symbol:** MANTA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.7281 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8763 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -1.6127 |
| sortino_ratio | -0.3718 |
| max_drawdown | 0.3643 |
| cagr | -0.1573 |
| net_avg_win | 76.0451 |
| net_avg_loss | -91.7605 |
| avg_hold_time_bars | 36.4943 |
| exposure | 0.4363 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
