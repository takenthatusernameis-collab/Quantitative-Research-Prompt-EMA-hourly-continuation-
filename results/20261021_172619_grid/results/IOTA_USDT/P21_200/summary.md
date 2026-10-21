# EMA Hourly Continuation — IOTA/USDT P21_200

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.9356 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1181 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -0.2969 |
| sortino_ratio | -0.0711 |
| max_drawdown | 0.1648 |
| cagr | -0.0360 |
| net_avg_win | 87.3619 |
| net_avg_loss | -104.8723 |
| avg_hold_time_bars | 50.4167 |
| exposure | 0.6325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
