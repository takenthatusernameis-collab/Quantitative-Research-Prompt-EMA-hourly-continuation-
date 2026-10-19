# EMA Hourly Continuation — BCH/USDT P20_200

**Symbol:** BCH/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6503 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 1.0298 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -2.4905 |
| sortino_ratio | -0.6104 |
| max_drawdown | 0.5612 |
| cagr | -0.2565 |
| net_avg_win | 64.2119 |
| net_avg_loss | -96.2160 |
| avg_hold_time_bars | 49.0649 |
| exposure | 0.6869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
