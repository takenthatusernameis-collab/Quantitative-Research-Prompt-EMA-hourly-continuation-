# EMA Hourly Continuation — LISTA/USDT P50_144

**Symbol:** LISTA/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.8009 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9847 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.3198 |
| sortino_ratio | -0.3543 |
| max_drawdown | 0.3524 |
| cagr | -0.1517 |
| net_avg_win | 78.6901 |
| net_avg_loss | -97.0629 |
| avg_hold_time_bars | 19.6463 |
| exposure | 0.3151 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
