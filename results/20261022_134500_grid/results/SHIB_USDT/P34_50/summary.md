# EMA Hourly Continuation — SHIB/USDT P34_50

**Symbol:** SHIB/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 945 |
| net_profit_factor | 0.3480 |
| net_win_rate | 0.4063 |
| gross_profit_factor | 0.8253 |
| gross_win_rate | 0.4349 |
| sharpe_ratio | -10.9097 |
| sortino_ratio | -4.8314 |
| max_drawdown | 0.9981 |
| cagr | -0.9160 |
| net_avg_win | 13.8724 |
| net_avg_loss | -27.2854 |
| avg_hold_time_bars | 2.4741 |
| exposure | 0.1063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
