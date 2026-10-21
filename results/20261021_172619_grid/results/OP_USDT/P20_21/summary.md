# EMA Hourly Continuation — OP/USDT P20_21

**Symbol:** OP/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 123 |
| net_profit_factor | 0.8844 |
| net_win_rate | 0.5528 |
| gross_profit_factor | 1.2241 |
| gross_win_rate | 0.5528 |
| sharpe_ratio | -0.3852 |
| sortino_ratio | -0.0621 |
| max_drawdown | 0.1220 |
| cagr | -0.0289 |
| net_avg_win | 79.8034 |
| net_avg_loss | -111.5690 |
| avg_hold_time_bars | 4.4309 |
| exposure | 0.0248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
