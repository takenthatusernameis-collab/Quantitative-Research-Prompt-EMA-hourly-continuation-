# EMA Hourly Continuation — BTT/USDT P21_55

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.4452 |
| net_win_rate | 0.4109 |
| gross_profit_factor | 0.7413 |
| gross_win_rate | 0.4109 |
| sharpe_ratio | -6.1740 |
| sortino_ratio | -1.9466 |
| max_drawdown | 0.9004 |
| cagr | -0.6009 |
| net_avg_win | 36.8644 |
| net_avg_loss | -57.7556 |
| avg_hold_time_bars | 9.8826 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
