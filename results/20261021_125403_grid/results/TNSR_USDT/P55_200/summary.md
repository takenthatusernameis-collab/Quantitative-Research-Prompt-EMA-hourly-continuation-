# EMA Hourly Continuation — TNSR/USDT P55_200

**Symbol:** TNSR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7702 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -1.4152 |
| sortino_ratio | -0.3521 |
| max_drawdown | 0.3467 |
| cagr | -0.1501 |
| net_avg_win | 76.2347 |
| net_avg_loss | -92.7107 |
| avg_hold_time_bars | 27.8072 |
| exposure | 0.3851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
