# EMA Hourly Continuation — MAGIC/USDT P144_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.6901 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9484 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -1.8955 |
| sortino_ratio | -0.4335 |
| max_drawdown | 0.4239 |
| cagr | -0.1808 |
| net_avg_win | 70.7608 |
| net_avg_loss | -97.0525 |
| avg_hold_time_bars | 7.1725 |
| exposure | 0.0831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
