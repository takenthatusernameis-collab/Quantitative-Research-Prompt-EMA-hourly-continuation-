# EMA Hourly Continuation — TURBO/USDT P12_20

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1285 |
| net_profit_factor | 0.3733 |
| net_win_rate | 0.3922 |
| gross_profit_factor | 0.6946 |
| gross_win_rate | 0.4241 |
| sharpe_ratio | -13.0140 |
| sortino_ratio | -7.2688 |
| max_drawdown | 0.9995 |
| cagr | -0.9747 |
| net_avg_win | 11.8138 |
| net_avg_loss | -20.4220 |
| avg_hold_time_bars | 2.0716 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
