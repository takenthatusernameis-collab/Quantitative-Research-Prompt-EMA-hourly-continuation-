# EMA Hourly Continuation — CETUS/USDT P12_20

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.6802 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9589 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -2.6198 |
| sortino_ratio | -0.7250 |
| max_drawdown | 0.5815 |
| cagr | -0.2835 |
| net_avg_win | 67.2080 |
| net_avg_loss | -90.7365 |
| avg_hold_time_bars | 4.5213 |
| exposure | 0.0769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
