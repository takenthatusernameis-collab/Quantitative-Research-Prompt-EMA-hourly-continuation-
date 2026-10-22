# EMA Hourly Continuation — LUNC/USDT P12_144

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 643 |
| net_profit_factor | 0.5376 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8586 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -4.7127 |
| sortino_ratio | -1.6719 |
| max_drawdown | 0.8720 |
| cagr | -0.5549 |
| net_avg_win | 34.7221 |
| net_avg_loss | -53.3940 |
| avg_hold_time_bars | 20.7574 |
| exposure | 0.6067 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
