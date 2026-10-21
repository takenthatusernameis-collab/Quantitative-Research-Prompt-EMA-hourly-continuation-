# EMA Hourly Continuation — CSPR/USDT P50_89

**Symbol:** CSPR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9639 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.7104 |
| sortino_ratio | -0.4389 |
| max_drawdown | 0.3971 |
| cagr | -0.1825 |
| net_avg_win | 68.3942 |
| net_avg_loss | -90.6594 |
| avg_hold_time_bars | 7.0280 |
| exposure | 0.1025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
