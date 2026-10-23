# EMA Hourly Continuation — API3/USDT P26_55

**Symbol:** API3/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 919 |
| net_profit_factor | 0.5346 |
| net_win_rate | 0.4483 |
| gross_profit_factor | 0.9394 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -6.9569 |
| sortino_ratio | -2.9773 |
| max_drawdown | 0.9743 |
| cagr | -0.7648 |
| net_avg_win | 27.1417 |
| net_avg_loss | -41.2594 |
| avg_hold_time_bars | 4.7682 |
| exposure | 0.1992 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
