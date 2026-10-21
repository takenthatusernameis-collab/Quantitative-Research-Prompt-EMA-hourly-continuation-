# EMA Hourly Continuation — AURORA/USDT P8_34

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9262 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -4.5873 |
| sortino_ratio | -1.7214 |
| max_drawdown | 0.8796 |
| cagr | -0.5507 |
| net_avg_win | 53.4882 |
| net_avg_loss | -66.6342 |
| avg_hold_time_bars | 9.7055 |
| exposure | 0.3070 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
