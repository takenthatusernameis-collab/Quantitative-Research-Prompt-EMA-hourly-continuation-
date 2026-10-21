# EMA Hourly Continuation — ASTR/USDT P12_20

**Symbol:** ASTR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6270 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -3.6418 |
| sortino_ratio | -1.1309 |
| max_drawdown | 0.7437 |
| cagr | -0.4076 |
| net_avg_win | 54.2922 |
| net_avg_loss | -80.5521 |
| avg_hold_time_bars | 5.4289 |
| exposure | 0.1157 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
