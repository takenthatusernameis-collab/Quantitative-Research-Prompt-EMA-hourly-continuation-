# EMA Hourly Continuation — ALEX/USDT P8_55

**Symbol:** ALEX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 809 |
| net_profit_factor | 0.6146 |
| net_win_rate | 0.4450 |
| gross_profit_factor | 0.9907 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -5.4721 |
| sortino_ratio | -2.1641 |
| max_drawdown | 0.9382 |
| cagr | -0.6589 |
| net_avg_win | 41.3176 |
| net_avg_loss | -53.9043 |
| avg_hold_time_bars | 14.7824 |
| exposure | 0.5436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
