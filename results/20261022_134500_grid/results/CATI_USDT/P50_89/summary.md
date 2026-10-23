# EMA Hourly Continuation — CATI/USDT P50_89

**Symbol:** CATI/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 640 |
| net_profit_factor | 0.5217 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.9772 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -6.3065 |
| sortino_ratio | -2.4641 |
| max_drawdown | 0.9234 |
| cagr | -0.7022 |
| net_avg_win | 33.7821 |
| net_avg_loss | -56.0660 |
| avg_hold_time_bars | 4.5359 |
| exposure | 0.1591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
