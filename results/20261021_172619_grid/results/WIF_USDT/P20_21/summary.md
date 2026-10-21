# EMA Hourly Continuation — WIF/USDT P20_21

**Symbol:** WIF/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 101 |
| net_profit_factor | 0.8672 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1040 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.4559 |
| sortino_ratio | -0.0660 |
| max_drawdown | 0.1694 |
| cagr | -0.0306 |
| net_avg_win | 92.5496 |
| net_avg_loss | -117.8398 |
| avg_hold_time_bars | 5.2178 |
| exposure | 0.0240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
