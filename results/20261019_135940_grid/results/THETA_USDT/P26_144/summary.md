# EMA Hourly Continuation — THETA/USDT P26_144

**Symbol:** THETA/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6166 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4743 |
| sharpe_ratio | -3.1367 |
| sortino_ratio | -0.9784 |
| max_drawdown | 0.6947 |
| cagr | -0.3692 |
| net_avg_win | 47.9317 |
| net_avg_loss | -69.5724 |
| avg_hold_time_bars | 20.4230 |
| exposure | 0.4521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
