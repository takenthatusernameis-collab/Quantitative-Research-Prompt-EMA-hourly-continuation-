# EMA Hourly Continuation — CGPT/USDT P12_21

**Symbol:** CGPT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1415 |
| net_profit_factor | 0.3340 |
| net_win_rate | 0.3993 |
| gross_profit_factor | 0.8872 |
| gross_win_rate | 0.4297 |
| sharpe_ratio | -12.9007 |
| sortino_ratio | -6.8984 |
| max_drawdown | 0.9999 |
| cagr | -0.9713 |
| net_avg_win | 8.8735 |
| net_avg_loss | -17.6614 |
| avg_hold_time_bars | 2.3519 |
| exposure | 0.1513 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
