# EMA Hourly Continuation — CATI/USDT P26_200

**Symbol:** CATI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6250 |
| net_win_rate | 0.4417 |
| gross_profit_factor | 0.7616 |
| gross_win_rate | 0.4417 |
| sharpe_ratio | -2.4043 |
| sortino_ratio | -0.5777 |
| max_drawdown | 0.4773 |
| cagr | -0.2344 |
| net_avg_win | 67.0680 |
| net_avg_loss | -84.8908 |
| avg_hold_time_bars | 46.1333 |
| exposure | 0.6069 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
