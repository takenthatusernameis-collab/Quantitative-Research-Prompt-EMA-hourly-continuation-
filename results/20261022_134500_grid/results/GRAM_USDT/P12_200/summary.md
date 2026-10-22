# EMA Hourly Continuation — GRAM/USDT P12_200

**Symbol:** GRAM/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5306 |
| net_win_rate | 0.4550 |
| gross_profit_factor | 0.8579 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -3.8140 |
| sortino_ratio | -1.0892 |
| max_drawdown | 0.7491 |
| cagr | -0.4066 |
| net_avg_win | 44.1470 |
| net_avg_loss | -69.4597 |
| avg_hold_time_bars | 38.5937 |
| exposure | 0.7210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
