# EMA Hourly Continuation — COTI/USDT P34_50

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.7412 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9907 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -1.4167 |
| sortino_ratio | -0.3049 |
| max_drawdown | 0.3385 |
| cagr | -0.1302 |
| net_avg_win | 75.5527 |
| net_avg_loss | -101.0359 |
| avg_hold_time_bars | 5.6844 |
| exposure | 0.0581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
