# EMA Hourly Continuation — KNC/USDT P12_144

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 361 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 1.0383 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -2.1085 |
| sortino_ratio | -0.5591 |
| max_drawdown | 0.5334 |
| cagr | -0.2393 |
| net_avg_win | 70.9771 |
| net_avg_loss | -98.0327 |
| avg_hold_time_bars | 46.4349 |
| exposure | 0.7620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
