# EMA Hourly Continuation — DEGEN/USDT P21_34

**Symbol:** DEGEN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1074 |
| net_profit_factor | 0.5186 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.8387 |
| gross_win_rate | 0.4534 |
| sharpe_ratio | -8.0493 |
| sortino_ratio | -3.7125 |
| max_drawdown | 0.9900 |
| cagr | -0.8400 |
| net_avg_win | 22.4997 |
| net_avg_loss | -34.2730 |
| avg_hold_time_bars | 3.0186 |
| exposure | 0.1476 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
