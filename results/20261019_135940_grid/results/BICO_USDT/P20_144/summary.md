# EMA Hourly Continuation — BICO/USDT P20_144

**Symbol:** BICO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.6674 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8673 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -2.7211 |
| sortino_ratio | -0.8123 |
| max_drawdown | 0.6436 |
| cagr | -0.3168 |
| net_avg_win | 59.9991 |
| net_avg_loss | -76.5246 |
| avg_hold_time_bars | 27.8996 |
| exposure | 0.5681 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
