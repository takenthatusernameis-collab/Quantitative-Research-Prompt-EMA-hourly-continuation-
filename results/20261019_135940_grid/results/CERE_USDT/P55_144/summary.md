# EMA Hourly Continuation — CERE/USDT P55_144

**Symbol:** CERE/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.4718 |
| net_win_rate | 0.3294 |
| gross_profit_factor | 0.7569 |
| gross_win_rate | 0.3498 |
| sharpe_ratio | -9.0031 |
| sortino_ratio | -3.1046 |
| max_drawdown | 0.9833 |
| cagr | -0.8003 |
| net_avg_win | 45.4677 |
| net_avg_loss | -47.3288 |
| avg_hold_time_bars | 10.2730 |
| exposure | 0.2736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
