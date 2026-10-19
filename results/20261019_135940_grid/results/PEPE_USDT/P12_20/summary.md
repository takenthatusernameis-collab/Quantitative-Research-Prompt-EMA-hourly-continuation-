# EMA Hourly Continuation — PEPE/USDT P12_20

**Symbol:** PEPE/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1471 |
| net_profit_factor | 0.3623 |
| net_win_rate | 0.3977 |
| gross_profit_factor | 0.7189 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -13.5246 |
| sortino_ratio | -7.3662 |
| max_drawdown | 0.9999 |
| cagr | -0.9793 |
| net_avg_win | 9.7115 |
| net_avg_loss | -17.6982 |
| avg_hold_time_bars | 1.9259 |
| exposure | 0.1288 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
