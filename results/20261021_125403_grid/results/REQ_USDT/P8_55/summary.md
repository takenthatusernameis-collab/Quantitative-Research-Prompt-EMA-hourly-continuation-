# EMA Hourly Continuation — REQ/USDT P8_55

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.5771 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.8101 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -5.5245 |
| sortino_ratio | -2.0988 |
| max_drawdown | 0.9162 |
| cagr | -0.6247 |
| net_avg_win | 40.7916 |
| net_avg_loss | -52.8827 |
| avg_hold_time_bars | 13.9958 |
| exposure | 0.4549 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
