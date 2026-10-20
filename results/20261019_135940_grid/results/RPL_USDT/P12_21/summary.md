# EMA Hourly Continuation — RPL/USDT P12_21

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1305 |
| net_profit_factor | 0.4116 |
| net_win_rate | 0.4460 |
| gross_profit_factor | 0.9346 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -9.5936 |
| sortino_ratio | -4.8930 |
| max_drawdown | 0.9978 |
| cagr | -0.9120 |
| net_avg_win | 11.9942 |
| net_avg_loss | -23.4563 |
| avg_hold_time_bars | 3.2123 |
| exposure | 0.1897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
