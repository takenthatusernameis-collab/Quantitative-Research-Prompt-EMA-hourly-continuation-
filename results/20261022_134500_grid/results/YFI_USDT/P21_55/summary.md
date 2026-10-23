# EMA Hourly Continuation — YFI/USDT P21_55

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1082 |
| net_profit_factor | 0.4559 |
| net_win_rate | 0.4270 |
| gross_profit_factor | 1.0436 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -9.7140 |
| sortino_ratio | -4.5010 |
| max_drawdown | 0.9971 |
| cagr | -0.8982 |
| net_avg_win | 18.0792 |
| net_avg_loss | -29.5502 |
| avg_hold_time_bars | 4.8614 |
| exposure | 0.2380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
