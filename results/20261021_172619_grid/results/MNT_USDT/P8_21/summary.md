# EMA Hourly Continuation — MNT/USDT P8_21

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.5757 |
| net_win_rate | 0.4744 |
| gross_profit_factor | 0.8914 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -4.4111 |
| sortino_ratio | -1.6079 |
| max_drawdown | 0.8448 |
| cagr | -0.5220 |
| net_avg_win | 37.3997 |
| net_avg_loss | -58.6373 |
| avg_hold_time_bars | 6.4667 |
| exposure | 0.1896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
