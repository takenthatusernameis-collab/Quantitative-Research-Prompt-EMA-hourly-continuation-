# EMA Hourly Continuation — FIDA/USDT P12_89

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.5559 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8490 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -4.3952 |
| sortino_ratio | -1.6609 |
| max_drawdown | 0.8700 |
| cagr | -0.5484 |
| net_avg_win | 32.1489 |
| net_avg_loss | -49.7148 |
| avg_hold_time_bars | 16.7023 |
| exposure | 0.5510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
