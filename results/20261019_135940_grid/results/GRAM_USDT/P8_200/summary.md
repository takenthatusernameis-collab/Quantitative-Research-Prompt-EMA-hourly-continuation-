# EMA Hourly Continuation — GRAM/USDT P8_200

**Symbol:** GRAM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5910 |
| net_win_rate | 0.4884 |
| gross_profit_factor | 0.9793 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -3.2319 |
| sortino_ratio | -0.8865 |
| max_drawdown | 0.6878 |
| cagr | -0.3537 |
| net_avg_win | 50.9089 |
| net_avg_loss | -82.2250 |
| avg_hold_time_bars | 45.3385 |
| exposure | 0.7975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
