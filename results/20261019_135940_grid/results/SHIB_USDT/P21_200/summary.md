# EMA Hourly Continuation — SHIB/USDT P21_200

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.6633 |
| net_win_rate | 0.4928 |
| gross_profit_factor | 1.0267 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.8128 |
| sortino_ratio | -0.7962 |
| max_drawdown | 0.6412 |
| cagr | -0.3250 |
| net_avg_win | 60.2807 |
| net_avg_loss | -88.2974 |
| avg_hold_time_bars | 30.2019 |
| exposure | 0.5711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
