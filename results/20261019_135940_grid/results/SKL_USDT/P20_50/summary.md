# EMA Hourly Continuation — SKL/USDT P20_50

**Symbol:** SKL/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1032 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -6.6409 |
| sortino_ratio | -3.0229 |
| max_drawdown | 0.9747 |
| cagr | -0.7638 |
| net_avg_win | 22.8577 |
| net_avg_loss | -37.5091 |
| avg_hold_time_bars | 4.7984 |
| exposure | 0.2251 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
