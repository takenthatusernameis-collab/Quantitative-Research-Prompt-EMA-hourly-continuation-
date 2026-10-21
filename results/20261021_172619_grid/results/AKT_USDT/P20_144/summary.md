# EMA Hourly Continuation — AKT/USDT P20_144

**Symbol:** AKT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.9005 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0530 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -0.6269 |
| sortino_ratio | -0.1736 |
| max_drawdown | 0.2324 |
| cagr | -0.0805 |
| net_avg_win | 90.0599 |
| net_avg_loss | -105.5308 |
| avg_hold_time_bars | 30.2527 |
| exposure | 0.5115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
