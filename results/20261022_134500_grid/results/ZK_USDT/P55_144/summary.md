# EMA Hourly Continuation — ZK/USDT P55_144

**Symbol:** ZK/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.5647 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -3.9310 |
| sortino_ratio | -1.2789 |
| max_drawdown | 0.7676 |
| cagr | -0.4571 |
| net_avg_win | 43.2820 |
| net_avg_loss | -64.4865 |
| avg_hold_time_bars | 11.0461 |
| exposure | 0.2687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
