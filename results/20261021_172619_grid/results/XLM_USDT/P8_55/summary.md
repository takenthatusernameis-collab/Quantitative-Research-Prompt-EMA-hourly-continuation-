# EMA Hourly Continuation — XLM/USDT P8_55

**Symbol:** XLM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 671 |
| net_profit_factor | 0.7505 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.9807 |
| sortino_ratio | -0.7375 |
| max_drawdown | 0.5926 |
| cagr | -0.2879 |
| net_avg_win | 50.0290 |
| net_avg_loss | -70.5451 |
| avg_hold_time_bars | 14.7988 |
| exposure | 0.4514 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
