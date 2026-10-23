# EMA Hourly Continuation — MAGIC/USDT P12_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.7184 |
| net_win_rate | 0.4683 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4762 |
| sharpe_ratio | -2.3090 |
| sortino_ratio | -0.6354 |
| max_drawdown | 0.6171 |
| cagr | -0.2565 |
| net_avg_win | 75.6750 |
| net_avg_loss | -92.7552 |
| avg_hold_time_bars | 43.1825 |
| exposure | 0.7420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
