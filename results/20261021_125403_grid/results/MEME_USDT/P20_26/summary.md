# EMA Hourly Continuation — MEME/USDT P20_26

**Symbol:** MEME/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.6351 |
| net_win_rate | 0.4647 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -2.4105 |
| sortino_ratio | -0.5355 |
| max_drawdown | 0.5213 |
| cagr | -0.2175 |
| net_avg_win | 71.4741 |
| net_avg_loss | -97.7037 |
| avg_hold_time_bars | 4.9378 |
| exposure | 0.0541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
