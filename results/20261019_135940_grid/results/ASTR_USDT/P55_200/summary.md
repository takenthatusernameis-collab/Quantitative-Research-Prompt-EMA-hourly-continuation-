# EMA Hourly Continuation — ASTR/USDT P55_200

**Symbol:** ASTR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 335 |
| net_profit_factor | 0.6802 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9769 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -2.1210 |
| sortino_ratio | -0.5509 |
| max_drawdown | 0.5123 |
| cagr | -0.2265 |
| net_avg_win | 61.4570 |
| net_avg_loss | -87.6980 |
| avg_hold_time_bars | 26.6597 |
| exposure | 0.4042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
