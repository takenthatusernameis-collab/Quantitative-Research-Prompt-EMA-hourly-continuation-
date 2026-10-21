# EMA Hourly Continuation — CRO/USDT P8_144

**Symbol:** CRO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8271 |
| net_win_rate | 0.5168 |
| gross_profit_factor | 1.0660 |
| gross_win_rate | 0.5168 |
| sharpe_ratio | -1.0352 |
| sortino_ratio | -0.2690 |
| max_drawdown | 0.2980 |
| cagr | -0.1176 |
| net_avg_win | 76.3214 |
| net_avg_loss | -98.6999 |
| avg_hold_time_bars | 51.7676 |
| exposure | 0.7695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
