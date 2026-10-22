# EMA Hourly Continuation — LISTA/USDT P12_200

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.9552 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1302 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.2216 |
| sortino_ratio | -0.0615 |
| max_drawdown | 0.1650 |
| cagr | -0.0338 |
| net_avg_win | 89.8814 |
| net_avg_loss | -106.2964 |
| avg_hold_time_bars | 39.4145 |
| exposure | 0.6649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
