# EMA Hourly Continuation — UMA/USDT P26_144

**Symbol:** UMA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 522 |
| net_profit_factor | 0.6211 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -3.0398 |
| sortino_ratio | -0.9804 |
| max_drawdown | 0.6988 |
| cagr | -0.3712 |
| net_avg_win | 44.9346 |
| net_avg_loss | -67.0102 |
| avg_hold_time_bars | 19.2318 |
| exposure | 0.4563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
