# EMA Hourly Continuation — RSR/USDT P26_34

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 193 |
| net_profit_factor | 0.6725 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9057 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -1.7255 |
| sortino_ratio | -0.3426 |
| max_drawdown | 0.3525 |
| cagr | -0.1458 |
| net_avg_win | 72.9179 |
| net_avg_loss | -98.7718 |
| avg_hold_time_bars | 5.2280 |
| exposure | 0.0459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
