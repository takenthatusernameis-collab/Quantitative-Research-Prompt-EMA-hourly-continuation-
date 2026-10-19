# EMA Hourly Continuation — AAVE/USDT P34_55

**Symbol:** AAVE/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 920 |
| net_profit_factor | 0.3797 |
| net_win_rate | 0.4207 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4391 |
| sharpe_ratio | -9.2537 |
| sortino_ratio | -3.9627 |
| max_drawdown | 0.9941 |
| cagr | -0.8695 |
| net_avg_win | 15.7214 |
| net_avg_loss | -30.0638 |
| avg_hold_time_bars | 2.7446 |
| exposure | 0.1148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
