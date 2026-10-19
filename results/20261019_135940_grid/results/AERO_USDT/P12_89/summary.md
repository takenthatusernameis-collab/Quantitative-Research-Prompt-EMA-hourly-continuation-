# EMA Hourly Continuation — AERO/USDT P12_89

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0789 |
| gross_win_rate | 0.5184 |
| sharpe_ratio | -2.0371 |
| sortino_ratio | -0.7532 |
| max_drawdown | 0.6268 |
| cagr | -0.3000 |
| net_avg_win | 63.5350 |
| net_avg_loss | -85.1215 |
| avg_hold_time_bars | 16.7673 |
| exposure | 0.5175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
