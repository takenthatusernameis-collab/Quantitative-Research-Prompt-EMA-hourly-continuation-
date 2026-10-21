# EMA Hourly Continuation — METIS/USDT P12_89

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.7118 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8658 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -2.5291 |
| sortino_ratio | -0.8063 |
| max_drawdown | 0.6208 |
| cagr | -0.3096 |
| net_avg_win | 64.1886 |
| net_avg_loss | -77.2511 |
| avg_hold_time_bars | 23.2752 |
| exposure | 0.5343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
