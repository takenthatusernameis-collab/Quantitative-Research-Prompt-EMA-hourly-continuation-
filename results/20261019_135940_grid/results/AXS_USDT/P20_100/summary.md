# EMA Hourly Continuation — AXS/USDT P20_100

**Symbol:** AXS/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 599 |
| net_profit_factor | 0.7136 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 1.0678 |
| gross_win_rate | 0.5125 |
| sharpe_ratio | -2.7352 |
| sortino_ratio | -0.9470 |
| max_drawdown | 0.6896 |
| cagr | -0.3590 |
| net_avg_win | 56.0151 |
| net_avg_loss | -78.7552 |
| avg_hold_time_bars | 15.9666 |
| exposure | 0.4328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
