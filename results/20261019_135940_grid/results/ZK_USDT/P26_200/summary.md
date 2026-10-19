# EMA Hourly Continuation — ZK/USDT P26_200

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7308 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4947 |
| sharpe_ratio | -1.8903 |
| sortino_ratio | -0.5312 |
| max_drawdown | 0.4635 |
| cagr | -0.2254 |
| net_avg_win | 66.3996 |
| net_avg_loss | -87.9925 |
| avg_hold_time_bars | 31.3209 |
| exposure | 0.5711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
