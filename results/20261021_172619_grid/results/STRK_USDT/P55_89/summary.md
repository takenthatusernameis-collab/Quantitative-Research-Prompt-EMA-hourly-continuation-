# EMA Hourly Continuation — STRK/USDT P55_89

**Symbol:** STRK/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6602 |
| net_win_rate | 0.4613 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4613 |
| sharpe_ratio | -2.2275 |
| sortino_ratio | -0.5467 |
| max_drawdown | 0.4973 |
| cagr | -0.2215 |
| net_avg_win | 66.2012 |
| net_avg_loss | -85.8610 |
| avg_hold_time_bars | 6.0000 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
