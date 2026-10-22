# EMA Hourly Continuation — SHIB/USDT P12_200

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.5781 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8981 |
| gross_win_rate | 0.4725 |
| sharpe_ratio | -3.1958 |
| sortino_ratio | -0.8184 |
| max_drawdown | 0.6566 |
| cagr | -0.3371 |
| net_avg_win | 54.7973 |
| net_avg_loss | -82.9389 |
| avg_hold_time_bars | 48.2899 |
| exposure | 0.7573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
