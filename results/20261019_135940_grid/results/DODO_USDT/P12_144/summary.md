# EMA Hourly Continuation — DODO/USDT P12_144

**Symbol:** DODO/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5335 |
| net_win_rate | 0.4085 |
| gross_profit_factor | 0.7620 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -5.5022 |
| sortino_ratio | -1.9332 |
| max_drawdown | 0.9075 |
| cagr | -0.6034 |
| net_avg_win | 39.8767 |
| net_avg_loss | -51.6213 |
| avg_hold_time_bars | 21.1688 |
| exposure | 0.6073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
