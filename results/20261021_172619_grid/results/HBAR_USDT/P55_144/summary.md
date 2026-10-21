# EMA Hourly Continuation — HBAR/USDT P55_144

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7949 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0291 |
| gross_win_rate | 0.5090 |
| sharpe_ratio | -1.3128 |
| sortino_ratio | -0.3447 |
| max_drawdown | 0.3501 |
| cagr | -0.1468 |
| net_avg_win | 74.9614 |
| net_avg_loss | -97.7505 |
| avg_hold_time_bars | 13.7575 |
| exposure | 0.2089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
