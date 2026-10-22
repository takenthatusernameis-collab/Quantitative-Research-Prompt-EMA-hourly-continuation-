# EMA Hourly Continuation — CFX/USDT P50_100

**Symbol:** CFX/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5122 |
| net_win_rate | 0.4579 |
| gross_profit_factor | 0.8235 |
| gross_win_rate | 0.4642 |
| sharpe_ratio | -4.9628 |
| sortino_ratio | -1.7592 |
| max_drawdown | 0.8843 |
| cagr | -0.5698 |
| net_avg_win | 32.0796 |
| net_avg_loss | -52.8935 |
| avg_hold_time_bars | 6.0302 |
| exposure | 0.1724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
