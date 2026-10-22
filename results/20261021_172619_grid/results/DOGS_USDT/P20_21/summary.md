# EMA Hourly Continuation — DOGS/USDT P20_21

**Symbol:** DOGS/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 76 |
| net_profit_factor | 0.7020 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9369 |
| gross_win_rate | 0.4868 |
| sharpe_ratio | -1.0035 |
| sortino_ratio | -0.1353 |
| max_drawdown | 0.1247 |
| cagr | -0.0600 |
| net_avg_win | 79.3639 |
| net_avg_loss | -107.2591 |
| avg_hold_time_bars | 4.5789 |
| exposure | 0.0185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
