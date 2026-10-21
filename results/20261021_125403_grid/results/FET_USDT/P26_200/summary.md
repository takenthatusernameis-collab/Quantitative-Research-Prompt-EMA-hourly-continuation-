# EMA Hourly Continuation — FET/USDT P26_200

**Symbol:** FET/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.9919 |
| net_win_rate | 0.5338 |
| gross_profit_factor | 1.1262 |
| gross_win_rate | 0.5338 |
| sharpe_ratio | 0.0100 |
| sortino_ratio | 0.0023 |
| max_drawdown | 0.1393 |
| cagr | -0.0042 |
| net_avg_win | 91.8766 |
| net_avg_loss | -106.0705 |
| avg_hold_time_bars | 49.3459 |
| exposure | 0.5966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
