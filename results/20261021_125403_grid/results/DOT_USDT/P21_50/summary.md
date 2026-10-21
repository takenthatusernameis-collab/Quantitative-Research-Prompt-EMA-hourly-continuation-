# EMA Hourly Continuation — DOT/USDT P21_50

**Symbol:** DOT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.8577 |
| net_win_rate | 0.5431 |
| gross_profit_factor | 1.1850 |
| gross_win_rate | 0.5431 |
| sharpe_ratio | -1.0180 |
| sortino_ratio | -0.3180 |
| max_drawdown | 0.3845 |
| cagr | -0.1372 |
| net_avg_win | 74.0689 |
| net_avg_loss | -102.6529 |
| avg_hold_time_bars | 7.4289 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
