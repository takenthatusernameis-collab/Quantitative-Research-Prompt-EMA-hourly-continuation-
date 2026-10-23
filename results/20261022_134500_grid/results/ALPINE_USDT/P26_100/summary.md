# EMA Hourly Continuation — ALPINE/USDT P26_100

**Symbol:** ALPINE/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.5579 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8775 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -5.4590 |
| sortino_ratio | -1.9732 |
| max_drawdown | 0.9181 |
| cagr | -0.6261 |
| net_avg_win | 37.8710 |
| net_avg_loss | -55.6588 |
| avg_hold_time_bars | 12.2245 |
| exposure | 0.3762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
