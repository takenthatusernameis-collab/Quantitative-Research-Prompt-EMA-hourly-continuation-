# EMA Hourly Continuation — MERL/USDT P50_200

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9304 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.3553 |
| sortino_ratio | -0.3392 |
| max_drawdown | 0.3527 |
| cagr | -0.1456 |
| net_avg_win | 82.5549 |
| net_avg_loss | -96.7235 |
| avg_hold_time_bars | 26.7240 |
| exposure | 0.3752 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
