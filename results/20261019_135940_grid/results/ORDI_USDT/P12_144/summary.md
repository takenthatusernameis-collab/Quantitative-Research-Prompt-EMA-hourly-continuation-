# EMA Hourly Continuation — ORDI/USDT P12_144

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 501 |
| net_profit_factor | 0.6356 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.8499 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -3.5025 |
| sortino_ratio | -1.1033 |
| max_drawdown | 0.7341 |
| cagr | -0.4039 |
| net_avg_win | 56.8831 |
| net_avg_loss | -71.7896 |
| avg_hold_time_bars | 29.8583 |
| exposure | 0.6800 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
