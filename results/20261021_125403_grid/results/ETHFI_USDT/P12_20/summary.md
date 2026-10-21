# EMA Hourly Continuation — ETHFI/USDT P12_20

**Symbol:** ETHFI/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 260 |
| net_profit_factor | 0.7255 |
| net_win_rate | 0.4808 |
| gross_profit_factor | 0.9235 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -1.6231 |
| sortino_ratio | -0.3739 |
| max_drawdown | 0.3730 |
| cagr | -0.1582 |
| net_avg_win | 74.2380 |
| net_avg_loss | -94.7413 |
| avg_hold_time_bars | 5.7769 |
| exposure | 0.0683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
