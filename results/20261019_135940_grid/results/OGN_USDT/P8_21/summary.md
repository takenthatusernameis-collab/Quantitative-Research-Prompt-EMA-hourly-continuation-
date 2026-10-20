# EMA Hourly Continuation — OGN/USDT P8_21

**Symbol:** OGN/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1573 |
| net_profit_factor | 0.4006 |
| net_win_rate | 0.4304 |
| gross_profit_factor | 0.9571 |
| gross_win_rate | 0.4768 |
| sharpe_ratio | -11.1798 |
| sortino_ratio | -6.2534 |
| max_drawdown | 0.9996 |
| cagr | -0.9557 |
| net_avg_win | 9.8680 |
| net_avg_loss | -18.6125 |
| avg_hold_time_bars | 3.4628 |
| exposure | 0.2465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
