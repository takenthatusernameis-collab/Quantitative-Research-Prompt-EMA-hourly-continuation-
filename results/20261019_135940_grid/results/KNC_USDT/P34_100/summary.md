# EMA Hourly Continuation — KNC/USDT P34_100

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 1.0006 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -4.7414 |
| sortino_ratio | -1.6199 |
| max_drawdown | 0.8647 |
| cagr | -0.5396 |
| net_avg_win | 46.7826 |
| net_avg_loss | -66.3911 |
| avg_hold_time_bars | 11.3396 |
| exposure | 0.3020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
