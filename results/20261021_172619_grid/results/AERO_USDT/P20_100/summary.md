# EMA Hourly Continuation — AERO/USDT P20_100

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 424 |
| net_profit_factor | 0.9721 |
| net_win_rate | 0.5354 |
| gross_profit_factor | 1.1436 |
| gross_win_rate | 0.5354 |
| sharpe_ratio | -0.1417 |
| sortino_ratio | -0.0422 |
| max_drawdown | 0.2416 |
| cagr | -0.0265 |
| net_avg_win | 100.0097 |
| net_avg_loss | -118.5505 |
| avg_hold_time_bars | 20.5542 |
| exposure | 0.3961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
