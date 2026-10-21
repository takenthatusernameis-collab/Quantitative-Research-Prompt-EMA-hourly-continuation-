# EMA Hourly Continuation — BABYDOGE/USDT P50_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 6 |
| net_profit_factor | 1.7864 |
| net_win_rate | 0.6667 |
| gross_profit_factor | 1.9811 |
| gross_win_rate | 0.6667 |
| sharpe_ratio | 0.4388 |
| sortino_ratio | 0.0165 |
| max_drawdown | 0.0109 |
| cagr | 0.0066 |
| net_avg_win | 95.3703 |
| net_avg_loss | -106.7720 |
| avg_hold_time_bars | 3.3333 |
| exposure | 0.0009 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
