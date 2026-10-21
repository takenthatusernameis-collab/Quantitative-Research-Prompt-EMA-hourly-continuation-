# EMA Hourly Continuation — JASMY/USDT P8_20

**Symbol:** JASMY/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.7145 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9324 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.1357 |
| sortino_ratio | -0.6101 |
| max_drawdown | 0.5325 |
| cagr | -0.2444 |
| net_avg_win | 65.5197 |
| net_avg_loss | -85.9095 |
| avg_hold_time_bars | 5.7243 |
| exposure | 0.1038 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
