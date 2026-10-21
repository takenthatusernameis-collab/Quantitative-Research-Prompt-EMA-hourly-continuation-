# EMA Hourly Continuation — T/USDT P21_144

**Symbol:** T/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.7807 |
| net_win_rate | 0.5099 |
| gross_profit_factor | 1.0343 |
| gross_win_rate | 0.5099 |
| sharpe_ratio | -1.5140 |
| sortino_ratio | -0.4348 |
| max_drawdown | 0.4034 |
| cagr | -0.1825 |
| net_avg_win | 68.8633 |
| net_avg_loss | -91.7679 |
| avg_hold_time_bars | 26.7921 |
| exposure | 0.4898 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
