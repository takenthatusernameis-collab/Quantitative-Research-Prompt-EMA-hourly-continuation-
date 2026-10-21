# EMA Hourly Continuation — CRV/USDT P21_34

**Symbol:** CRV/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.7083 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9661 |
| gross_win_rate | 0.4980 |
| sharpe_ratio | -1.5486 |
| sortino_ratio | -0.3479 |
| max_drawdown | 0.3668 |
| cagr | -0.1467 |
| net_avg_win | 65.4192 |
| net_avg_loss | -91.6067 |
| avg_hold_time_bars | 4.7061 |
| exposure | 0.0524 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
