# EMA Hourly Continuation — AUCTION/USDT P89_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.2369 |
| net_win_rate | 0.3547 |
| gross_profit_factor | 0.6394 |
| gross_win_rate | 0.4205 |
| sharpe_ratio | -10.1304 |
| sortino_ratio | -3.6683 |
| max_drawdown | 0.9929 |
| cagr | -0.8588 |
| net_avg_win | 13.9460 |
| net_avg_loss | -32.3639 |
| avg_hold_time_bars | 3.2135 |
| exposure | 0.0906 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
