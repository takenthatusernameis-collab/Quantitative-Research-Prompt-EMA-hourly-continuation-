# EMA Hourly Continuation — ORDI/USDT P26_144

**Symbol:** ORDI/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6365 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8602 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -3.5620 |
| sortino_ratio | -1.1839 |
| max_drawdown | 0.7603 |
| cagr | -0.4270 |
| net_avg_win | 52.1124 |
| net_avg_loss | -68.5914 |
| avg_hold_time_bars | 16.8216 |
| exposure | 0.4244 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
