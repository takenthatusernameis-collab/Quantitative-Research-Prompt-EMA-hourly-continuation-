# EMA Hourly Continuation — PROM/USDT P12_144

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4295 |
| gross_profit_factor | 0.7828 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -5.1845 |
| sortino_ratio | -1.8262 |
| max_drawdown | 0.8919 |
| cagr | -0.5832 |
| net_avg_win | 33.8633 |
| net_avg_loss | -50.1838 |
| avg_hold_time_bars | 21.2837 |
| exposure | 0.6105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
