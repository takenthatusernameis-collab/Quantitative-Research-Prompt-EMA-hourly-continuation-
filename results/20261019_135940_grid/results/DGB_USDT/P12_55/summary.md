# EMA Hourly Continuation — DGB/USDT P12_55

**Symbol:** DGB/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1083 |
| net_profit_factor | 0.5354 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.9396 |
| gross_win_rate | 0.4718 |
| sharpe_ratio | -6.8213 |
| sortino_ratio | -3.1379 |
| max_drawdown | 0.9805 |
| cagr | -0.7882 |
| net_avg_win | 22.7579 |
| net_avg_loss | -35.9199 |
| avg_hold_time_bars | 8.2502 |
| exposure | 0.4061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
