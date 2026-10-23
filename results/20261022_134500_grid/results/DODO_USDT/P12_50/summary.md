# EMA Hourly Continuation — DODO/USDT P12_50

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.5582 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.9203 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -6.8862 |
| sortino_ratio | -3.2295 |
| max_drawdown | 0.9807 |
| cagr | -0.7884 |
| net_avg_win | 24.7144 |
| net_avg_loss | -36.0701 |
| avg_hold_time_bars | 6.9964 |
| exposure | 0.3533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
