# EMA Hourly Continuation — ANYONE/USDT P12_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.7012 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8831 |
| gross_win_rate | 0.4675 |
| sharpe_ratio | -3.1852 |
| sortino_ratio | -1.2058 |
| max_drawdown | 0.7380 |
| cagr | -0.4318 |
| net_avg_win | 56.6017 |
| net_avg_loss | -69.5529 |
| avg_hold_time_bars | 15.9118 |
| exposure | 0.5194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
