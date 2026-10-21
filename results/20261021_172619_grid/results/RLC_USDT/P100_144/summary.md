# EMA Hourly Continuation — RLC/USDT P100_144

**Symbol:** RLC/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.7267 |
| net_win_rate | 0.5097 |
| gross_profit_factor | 1.0290 |
| gross_win_rate | 0.5097 |
| sharpe_ratio | -1.7388 |
| sortino_ratio | -0.4404 |
| max_drawdown | 0.4247 |
| cagr | -0.1833 |
| net_avg_win | 67.0860 |
| net_avg_loss | -95.9585 |
| avg_hold_time_bars | 5.9548 |
| exposure | 0.0839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
