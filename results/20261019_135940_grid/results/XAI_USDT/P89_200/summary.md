# EMA Hourly Continuation — XAI/USDT P89_200

**Symbol:** XAI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6436 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.9644 |
| gross_win_rate | 0.4935 |
| sharpe_ratio | -2.8269 |
| sortino_ratio | -0.7821 |
| max_drawdown | 0.6421 |
| cagr | -0.3132 |
| net_avg_win | 59.6141 |
| net_avg_loss | -84.8351 |
| avg_hold_time_bars | 13.0439 |
| exposure | 0.2295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
