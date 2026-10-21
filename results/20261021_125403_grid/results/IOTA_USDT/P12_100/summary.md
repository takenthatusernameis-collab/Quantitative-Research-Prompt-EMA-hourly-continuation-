# EMA Hourly Continuation — IOTA/USDT P12_100

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.8133 |
| net_win_rate | 0.5019 |
| gross_profit_factor | 1.0033 |
| gross_win_rate | 0.5019 |
| sharpe_ratio | -1.4584 |
| sortino_ratio | -0.4792 |
| max_drawdown | 0.4628 |
| cagr | -0.1992 |
| net_avg_win | 70.5595 |
| net_avg_loss | -87.4171 |
| avg_hold_time_bars | 22.7091 |
| exposure | 0.5430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
