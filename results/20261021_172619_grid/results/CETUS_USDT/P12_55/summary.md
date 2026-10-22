# EMA Hourly Continuation — CETUS/USDT P12_55

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.7856 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -2.2229 |
| sortino_ratio | -0.8099 |
| max_drawdown | 0.6389 |
| cagr | -0.3119 |
| net_avg_win | 70.5747 |
| net_avg_loss | -84.2534 |
| avg_hold_time_bars | 12.0595 |
| exposure | 0.3575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
