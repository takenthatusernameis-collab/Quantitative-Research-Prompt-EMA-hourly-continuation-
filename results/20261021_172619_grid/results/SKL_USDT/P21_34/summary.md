# EMA Hourly Continuation — SKL/USDT P21_34

**Symbol:** SKL/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 331 |
| net_profit_factor | 0.5635 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.7954 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -3.1745 |
| sortino_ratio | -0.8243 |
| max_drawdown | 0.6264 |
| cagr | -0.3148 |
| net_avg_win | 53.4795 |
| net_avg_loss | -76.7526 |
| avg_hold_time_bars | 4.8882 |
| exposure | 0.0735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
