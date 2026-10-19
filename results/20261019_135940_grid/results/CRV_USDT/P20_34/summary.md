# EMA Hourly Continuation — CRV/USDT P20_34

**Symbol:** CRV/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1157 |
| net_profit_factor | 0.4037 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.8612 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -9.1807 |
| sortino_ratio | -4.4128 |
| max_drawdown | 0.9963 |
| cagr | -0.8912 |
| net_avg_win | 13.0226 |
| net_avg_loss | -26.1465 |
| avg_hold_time_bars | 2.3967 |
| exposure | 0.1260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
