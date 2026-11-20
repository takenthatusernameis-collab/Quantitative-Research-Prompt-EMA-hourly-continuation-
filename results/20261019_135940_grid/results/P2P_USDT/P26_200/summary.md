# EMA Hourly Continuation — P2P/USDT P26_200

**Symbol:** P2P/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.6356 |
| net_win_rate | 0.4297 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4322 |
| sharpe_ratio | -3.0263 |
| sortino_ratio | -0.8424 |
| max_drawdown | 0.6689 |
| cagr | -0.3268 |
| net_avg_win | 65.3991 |
| net_avg_loss | -77.5114 |
| avg_hold_time_bars | 29.1688 |
| exposure | 0.5184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
