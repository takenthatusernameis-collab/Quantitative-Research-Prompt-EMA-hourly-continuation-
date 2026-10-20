# EMA Hourly Continuation — POLYX/USDT P12_26

**Symbol:** POLYX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1279 |
| net_profit_factor | 0.4334 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.8597 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -9.6196 |
| sortino_ratio | -4.8725 |
| max_drawdown | 0.9977 |
| cagr | -0.9100 |
| net_avg_win | 13.5291 |
| net_avg_loss | -24.6249 |
| avg_hold_time_bars | 3.6278 |
| exposure | 0.2109 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
