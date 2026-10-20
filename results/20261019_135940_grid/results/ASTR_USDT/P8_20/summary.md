# EMA Hourly Continuation — ASTR/USDT P8_20

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1518 |
| net_profit_factor | 0.3610 |
| net_win_rate | 0.4420 |
| gross_profit_factor | 0.8794 |
| gross_win_rate | 0.4736 |
| sharpe_ratio | -11.1344 |
| sortino_ratio | -6.1120 |
| max_drawdown | 0.9996 |
| cagr | -0.9546 |
| net_avg_win | 8.4152 |
| net_avg_loss | -18.4682 |
| avg_hold_time_bars | 3.5356 |
| exposure | 0.2429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
