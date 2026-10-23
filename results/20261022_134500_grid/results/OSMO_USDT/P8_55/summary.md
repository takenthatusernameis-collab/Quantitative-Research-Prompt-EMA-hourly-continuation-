# EMA Hourly Continuation — OSMO/USDT P8_55

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 991 |
| net_profit_factor | 0.6528 |
| net_win_rate | 0.4541 |
| gross_profit_factor | 1.0363 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -6.0989 |
| sortino_ratio | -2.7075 |
| max_drawdown | 0.9625 |
| cagr | -0.7274 |
| net_avg_win | 40.1887 |
| net_avg_loss | -51.2061 |
| avg_hold_time_bars | 11.5943 |
| exposure | 0.5223 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
