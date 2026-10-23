# EMA Hourly Continuation — BLZ/USDT P21_50

**Symbol:** BLZ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1049 |
| net_profit_factor | 0.4592 |
| net_win_rate | 0.4128 |
| gross_profit_factor | 0.8271 |
| gross_win_rate | 0.4299 |
| sharpe_ratio | -8.8162 |
| sortino_ratio | -4.0233 |
| max_drawdown | 0.9929 |
| cagr | -0.8595 |
| net_avg_win | 19.4734 |
| net_avg_loss | -29.8071 |
| avg_hold_time_bars | 5.1754 |
| exposure | 0.2457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
