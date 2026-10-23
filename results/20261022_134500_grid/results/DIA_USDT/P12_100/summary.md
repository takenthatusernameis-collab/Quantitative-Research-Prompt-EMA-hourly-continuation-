# EMA Hourly Continuation — DIA/USDT P12_100

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 703 |
| net_profit_factor | 0.5820 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8470 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -4.7868 |
| sortino_ratio | -1.7674 |
| max_drawdown | 0.8933 |
| cagr | -0.5767 |
| net_avg_win | 39.1468 |
| net_avg_loss | -54.6081 |
| avg_hold_time_bars | 16.8279 |
| exposure | 0.5353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
