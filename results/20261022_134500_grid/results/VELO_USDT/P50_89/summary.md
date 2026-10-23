# EMA Hourly Continuation — VELO/USDT P50_89

**Symbol:** VELO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9599 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -4.0932 |
| sortino_ratio | -1.5511 |
| max_drawdown | 0.8517 |
| cagr | -0.5214 |
| net_avg_win | 41.9300 |
| net_avg_loss | -62.6124 |
| avg_hold_time_bars | 4.6175 |
| exposure | 0.1509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
