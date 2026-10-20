# EMA Hourly Continuation — MANTA/USDT P89_200

**Symbol:** MANTA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6601 |
| net_win_rate | 0.4850 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.6925 |
| sortino_ratio | -0.7584 |
| max_drawdown | 0.6062 |
| cagr | -0.3026 |
| net_avg_win | 59.6180 |
| net_avg_loss | -85.0527 |
| avg_hold_time_bars | 11.5625 |
| exposure | 0.2102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
