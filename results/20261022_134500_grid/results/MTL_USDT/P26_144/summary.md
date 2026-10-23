# EMA Hourly Continuation — MTL/USDT P26_144

**Symbol:** MTL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 457 |
| net_profit_factor | 0.5267 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8042 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.3189 |
| sortino_ratio | -1.2893 |
| max_drawdown | 0.8040 |
| cagr | -0.4675 |
| net_avg_win | 44.0643 |
| net_avg_loss | -65.6896 |
| avg_hold_time_bars | 25.5777 |
| exposure | 0.5290 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
