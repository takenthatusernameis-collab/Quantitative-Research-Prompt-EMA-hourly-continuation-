# EMA Hourly Continuation — DOT/USDT P20_50

**Symbol:** DOT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 963 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9938 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -6.3546 |
| sortino_ratio | -2.7832 |
| max_drawdown | 0.9688 |
| cagr | -0.7431 |
| net_avg_win | 23.0711 |
| net_avg_loss | -40.7049 |
| avg_hold_time_bars | 4.6677 |
| exposure | 0.2043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
