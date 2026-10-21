# EMA Hourly Continuation — POL/USDT P12_20

**Symbol:** POL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.5573 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8112 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -2.7046 |
| sortino_ratio | -0.6312 |
| max_drawdown | 0.5370 |
| cagr | -0.2504 |
| net_avg_win | 53.1524 |
| net_avg_loss | -80.7996 |
| avg_hold_time_bars | 5.2594 |
| exposure | 0.0636 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
