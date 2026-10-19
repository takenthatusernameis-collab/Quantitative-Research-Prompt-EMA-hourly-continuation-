# EMA Hourly Continuation — BSV/USDT P12_26

**Symbol:** BSV/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1521 |
| net_profit_factor | 0.2818 |
| net_win_rate | 0.3787 |
| gross_profit_factor | 0.7728 |
| gross_win_rate | 0.4201 |
| sharpe_ratio | -14.3343 |
| sortino_ratio | -8.0303 |
| max_drawdown | 1.0000 |
| cagr | -0.9832 |
| net_avg_win | 6.8131 |
| net_avg_loss | -14.7344 |
| avg_hold_time_bars | 2.8797 |
| exposure | 0.1991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
