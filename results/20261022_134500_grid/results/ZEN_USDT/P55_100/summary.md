# EMA Hourly Continuation — ZEN/USDT P55_100

**Symbol:** ZEN/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.5323 |
| net_win_rate | 0.4591 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4799 |
| sharpe_ratio | -5.1446 |
| sortino_ratio | -1.8841 |
| max_drawdown | 0.8999 |
| cagr | -0.5964 |
| net_avg_win | 33.0636 |
| net_avg_loss | -52.7265 |
| avg_hold_time_bars | 5.3982 |
| exposure | 0.1651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
