# EMA Hourly Continuation — ZEC/USDT P8_21

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1644 |
| net_profit_factor | 0.2667 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.6990 |
| gross_win_rate | 0.4568 |
| sharpe_ratio | -10.4470 |
| sortino_ratio | -5.9611 |
| max_drawdown | 0.9994 |
| cagr | -0.9477 |
| net_avg_win | 5.0552 |
| net_avg_loss | -14.7336 |
| avg_hold_time_bars | 2.8802 |
| exposure | 0.2152 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
