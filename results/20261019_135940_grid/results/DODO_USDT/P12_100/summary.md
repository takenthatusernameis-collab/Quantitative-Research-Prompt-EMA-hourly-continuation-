# EMA Hourly Continuation — DODO/USDT P12_100

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 770 |
| net_profit_factor | 0.6213 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.9200 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -4.8977 |
| sortino_ratio | -1.9135 |
| max_drawdown | 0.9092 |
| cagr | -0.5950 |
| net_avg_win | 42.5736 |
| net_avg_loss | -55.9149 |
| avg_hold_time_bars | 15.5234 |
| exposure | 0.5409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
