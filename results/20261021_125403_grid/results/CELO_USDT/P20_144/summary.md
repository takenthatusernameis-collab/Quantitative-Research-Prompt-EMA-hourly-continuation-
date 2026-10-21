# EMA Hourly Continuation — CELO/USDT P20_144

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.9006 |
| net_win_rate | 0.5210 |
| gross_profit_factor | 1.0939 |
| gross_win_rate | 0.5210 |
| sharpe_ratio | -0.6608 |
| sortino_ratio | -0.1792 |
| max_drawdown | 0.3614 |
| cagr | -0.0824 |
| net_avg_win | 94.9381 |
| net_avg_loss | -114.6639 |
| avg_hold_time_bars | 35.4146 |
| exposure | 0.5721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
