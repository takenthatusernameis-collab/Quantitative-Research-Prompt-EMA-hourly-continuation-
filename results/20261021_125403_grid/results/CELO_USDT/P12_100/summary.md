# EMA Hourly Continuation — CELO/USDT P12_100

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.8447 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0316 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.2482 |
| sortino_ratio | -0.3923 |
| max_drawdown | 0.4513 |
| cagr | -0.1675 |
| net_avg_win | 82.5020 |
| net_avg_loss | -99.7182 |
| avg_hold_time_bars | 27.2857 |
| exposure | 0.5964 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
