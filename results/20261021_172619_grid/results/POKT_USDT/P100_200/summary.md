# EMA Hourly Continuation — POKT/USDT P100_200

**Symbol:** POKT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.6029 |
| net_win_rate | 0.4184 |
| gross_profit_factor | 0.7773 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -3.0179 |
| sortino_ratio | -0.7297 |
| max_drawdown | 0.5905 |
| cagr | -0.2860 |
| net_avg_win | 70.6662 |
| net_avg_loss | -84.3089 |
| avg_hold_time_bars | 15.4354 |
| exposure | 0.2054 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
