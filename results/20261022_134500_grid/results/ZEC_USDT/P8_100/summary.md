# EMA Hourly Continuation — ZEC/USDT P8_100

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4712 |
| gross_profit_factor | 0.8929 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -3.7051 |
| sortino_ratio | -1.3381 |
| max_drawdown | 0.8162 |
| cagr | -0.4743 |
| net_avg_win | 39.9226 |
| net_avg_loss | -58.5287 |
| avg_hold_time_bars | 22.3424 |
| exposure | 0.6703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
