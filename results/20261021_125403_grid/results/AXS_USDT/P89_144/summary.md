# EMA Hourly Continuation — AXS/USDT P89_144

**Symbol:** AXS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.9011 |
| net_win_rate | 0.5510 |
| gross_profit_factor | 1.2141 |
| gross_win_rate | 0.5510 |
| sharpe_ratio | -0.4578 |
| sortino_ratio | -0.1038 |
| max_drawdown | 0.1620 |
| cagr | -0.0489 |
| net_avg_win | 80.2017 |
| net_avg_loss | -109.2298 |
| avg_hold_time_bars | 7.0694 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
