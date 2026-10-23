# EMA Hourly Continuation — WEMIX/USDT P21_50

**Symbol:** WEMIX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1449 |
| net_profit_factor | 0.1816 |
| net_win_rate | 0.2823 |
| gross_profit_factor | 0.4083 |
| gross_win_rate | 0.3016 |
| sharpe_ratio | -17.8799 |
| sortino_ratio | -9.9019 |
| max_drawdown | 1.0000 |
| cagr | -0.9945 |
| net_avg_win | 5.4258 |
| net_avg_loss | -11.7492 |
| avg_hold_time_bars | 4.2043 |
| exposure | 0.2769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
