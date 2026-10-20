# EMA Hourly Continuation — NYM/USDT P20_200

**Symbol:** NYM/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.3325 |
| net_win_rate | 0.3521 |
| gross_profit_factor | 0.5906 |
| gross_win_rate | 0.3662 |
| sharpe_ratio | -6.8508 |
| sortino_ratio | -1.9908 |
| max_drawdown | 0.9196 |
| cagr | -0.6331 |
| net_avg_win | 30.5367 |
| net_avg_loss | -49.9059 |
| avg_hold_time_bars | 30.2113 |
| exposure | 0.5850 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
