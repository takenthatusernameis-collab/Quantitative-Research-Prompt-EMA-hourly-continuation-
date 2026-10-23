# EMA Hourly Continuation — DEEP/USDT P26_34

**Symbol:** DEEP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 753 |
| net_profit_factor | 0.4488 |
| net_win_rate | 0.4290 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4555 |
| sharpe_ratio | -8.6896 |
| sortino_ratio | -3.7472 |
| max_drawdown | 0.9790 |
| cagr | -0.8520 |
| net_avg_win | 24.6686 |
| net_avg_loss | -41.2921 |
| avg_hold_time_bars | 2.2178 |
| exposure | 0.0946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
