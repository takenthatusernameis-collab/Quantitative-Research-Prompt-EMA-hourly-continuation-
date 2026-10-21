# EMA Hourly Continuation — ETC/USDT P8_26

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6558 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9880 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -3.4564 |
| sortino_ratio | -1.2688 |
| max_drawdown | 0.7713 |
| cagr | -0.4393 |
| net_avg_win | 45.1998 |
| net_avg_loss | -67.6633 |
| avg_hold_time_bars | 6.8543 |
| exposure | 0.2031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
