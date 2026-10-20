# EMA Hourly Continuation — TFUEL/USDT P12_20

**Symbol:** TFUEL/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1616 |
| net_profit_factor | 0.2681 |
| net_win_rate | 0.3533 |
| gross_profit_factor | 0.7134 |
| gross_win_rate | 0.4047 |
| sharpe_ratio | -16.7415 |
| sortino_ratio | -9.7166 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 6.4143 |
| net_avg_loss | -13.0742 |
| avg_hold_time_bars | 2.5000 |
| exposure | 0.1828 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
