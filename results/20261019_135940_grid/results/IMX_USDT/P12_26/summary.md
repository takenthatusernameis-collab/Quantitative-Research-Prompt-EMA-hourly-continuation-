# EMA Hourly Continuation — IMX/USDT P12_26

**Symbol:** IMX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1376 |
| net_profit_factor | 0.4606 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8730 |
| gross_win_rate | 0.4608 |
| sharpe_ratio | -9.7493 |
| sortino_ratio | -5.0617 |
| max_drawdown | 0.9984 |
| cagr | -0.9213 |
| net_avg_win | 14.0243 |
| net_avg_loss | -24.1021 |
| avg_hold_time_bars | 3.0531 |
| exposure | 0.1901 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
