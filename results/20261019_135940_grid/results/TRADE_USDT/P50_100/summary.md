# EMA Hourly Continuation — TRADE/USDT P50_100

**Symbol:** TRADE/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4064 |
| gross_profit_factor | 0.7302 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -5.7064 |
| sortino_ratio | -1.7931 |
| max_drawdown | 0.8968 |
| cagr | -0.5911 |
| net_avg_win | 38.2074 |
| net_avg_loss | -56.1611 |
| avg_hold_time_bars | 7.2211 |
| exposure | 0.1648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
