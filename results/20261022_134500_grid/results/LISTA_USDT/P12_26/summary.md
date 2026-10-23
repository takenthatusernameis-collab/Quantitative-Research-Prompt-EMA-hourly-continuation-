# EMA Hourly Continuation — LISTA/USDT P12_26

**Symbol:** LISTA/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1151 |
| net_profit_factor | 0.5220 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -8.3832 |
| sortino_ratio | -4.1651 |
| max_drawdown | 0.9913 |
| cagr | -0.8665 |
| net_avg_win | 21.6404 |
| net_avg_loss | -31.8424 |
| avg_hold_time_bars | 3.8132 |
| exposure | 0.2146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
