# EMA Hourly Continuation — BSV/USDT P26_50

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.3252 |
| net_win_rate | 0.3960 |
| gross_profit_factor | 0.7576 |
| gross_win_rate | 0.4284 |
| sharpe_ratio | -10.8391 |
| sortino_ratio | -4.9855 |
| max_drawdown | 0.9984 |
| cagr | -0.9218 |
| net_avg_win | 11.5917 |
| net_avg_loss | -23.3711 |
| avg_hold_time_bars | 3.7366 |
| exposure | 0.1780 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
