# EMA Hourly Continuation — ASTR/USDT P26_100

**Symbol:** ASTR/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 585 |
| net_profit_factor | 0.6186 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4872 |
| sharpe_ratio | -3.6914 |
| sortino_ratio | -1.2598 |
| max_drawdown | 0.7836 |
| cagr | -0.4494 |
| net_avg_win | 44.7568 |
| net_avg_loss | -67.3339 |
| avg_hold_time_bars | 14.5521 |
| exposure | 0.3852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
