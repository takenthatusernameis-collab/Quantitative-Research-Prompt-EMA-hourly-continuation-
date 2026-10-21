# EMA Hourly Continuation — ENJ/USDT P21_200

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.9269 |
| net_win_rate | 0.5245 |
| gross_profit_factor | 1.1038 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.3740 |
| sortino_ratio | -0.0908 |
| max_drawdown | 0.2600 |
| cagr | -0.0446 |
| net_avg_win | 91.9390 |
| net_avg_loss | -109.4032 |
| avg_hold_time_bars | 49.4510 |
| exposure | 0.6400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
