# EMA Hourly Continuation — ZK/USDT P34_144

**Symbol:** ZK/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6465 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.9019 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -3.2361 |
| sortino_ratio | -1.0548 |
| max_drawdown | 0.6970 |
| cagr | -0.3949 |
| net_avg_win | 53.5849 |
| net_avg_loss | -73.8185 |
| avg_hold_time_bars | 16.4711 |
| exposure | 0.4023 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
