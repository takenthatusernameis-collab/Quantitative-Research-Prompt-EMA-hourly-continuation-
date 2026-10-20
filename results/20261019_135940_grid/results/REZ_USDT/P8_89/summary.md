# EMA Hourly Continuation — REZ/USDT P8_89

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.7482 |
| net_win_rate | 0.4993 |
| gross_profit_factor | 1.0147 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -2.5912 |
| sortino_ratio | -0.9690 |
| max_drawdown | 0.7140 |
| cagr | -0.3722 |
| net_avg_win | 58.5590 |
| net_avg_loss | -78.0438 |
| avg_hold_time_bars | 19.6388 |
| exposure | 0.6297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
