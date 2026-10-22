# EMA Hourly Continuation — WLD/USDT P21_50

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.5602 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9219 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -5.3165 |
| sortino_ratio | -2.2677 |
| max_drawdown | 0.9394 |
| cagr | -0.6697 |
| net_avg_win | 26.8487 |
| net_avg_loss | -44.2496 |
| avg_hold_time_bars | 5.1953 |
| exposure | 0.2189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
