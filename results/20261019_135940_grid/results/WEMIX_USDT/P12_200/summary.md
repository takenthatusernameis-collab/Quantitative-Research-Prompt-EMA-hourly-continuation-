# EMA Hourly Continuation — WEMIX/USDT P12_200

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.3403 |
| net_win_rate | 0.3339 |
| gross_profit_factor | 0.4962 |
| gross_win_rate | 0.3374 |
| sharpe_ratio | -7.9026 |
| sortino_ratio | -2.6423 |
| max_drawdown | 0.9644 |
| cagr | -0.7321 |
| net_avg_win | 26.1528 |
| net_avg_loss | -38.5301 |
| avg_hold_time_bars | 29.0808 |
| exposure | 0.7521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
