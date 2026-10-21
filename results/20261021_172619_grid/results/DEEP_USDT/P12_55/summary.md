# EMA Hourly Continuation — DEEP/USDT P12_55

**Symbol:** DEEP/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.9571 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1385 |
| gross_win_rate | 0.5356 |
| sharpe_ratio | -0.2870 |
| sortino_ratio | -0.1025 |
| max_drawdown | 0.2483 |
| cagr | -0.0554 |
| net_avg_win | 92.4712 |
| net_avg_loss | -110.5386 |
| avg_hold_time_bars | 12.3951 |
| exposure | 0.3446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
