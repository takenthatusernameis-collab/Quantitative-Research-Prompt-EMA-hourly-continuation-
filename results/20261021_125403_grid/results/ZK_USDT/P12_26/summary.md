# EMA Hourly Continuation — ZK/USDT P12_26

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.7229 |
| net_win_rate | 0.4923 |
| gross_profit_factor | 0.9580 |
| gross_win_rate | 0.4923 |
| sharpe_ratio | -2.4061 |
| sortino_ratio | -0.8126 |
| max_drawdown | 0.6477 |
| cagr | -0.3107 |
| net_avg_win | 59.4953 |
| net_avg_loss | -79.7987 |
| avg_hold_time_bars | 4.9363 |
| exposure | 0.1247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
