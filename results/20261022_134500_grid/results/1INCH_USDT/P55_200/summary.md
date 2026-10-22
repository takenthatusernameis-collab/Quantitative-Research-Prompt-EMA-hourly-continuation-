# EMA Hourly Continuation — 1INCH/USDT P55_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.6588 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 1.0639 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -2.8667 |
| sortino_ratio | -0.8045 |
| max_drawdown | 0.6449 |
| cagr | -0.3273 |
| net_avg_win | 60.5861 |
| net_avg_loss | -90.1633 |
| avg_hold_time_bars | 20.2192 |
| exposure | 0.3731 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
