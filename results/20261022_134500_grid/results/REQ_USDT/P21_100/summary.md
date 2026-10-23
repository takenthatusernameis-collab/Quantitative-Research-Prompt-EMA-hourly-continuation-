# EMA Hourly Continuation — REQ/USDT P21_100

**Symbol:** REQ/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 798 |
| net_profit_factor | 0.4954 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.9380 |
| gross_win_rate | 0.4511 |
| sharpe_ratio | -7.5971 |
| sortino_ratio | -3.0182 |
| max_drawdown | 0.9784 |
| cagr | -0.7809 |
| net_avg_win | 28.4001 |
| net_avg_loss | -42.1268 |
| avg_hold_time_bars | 11.2644 |
| exposure | 0.4086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
