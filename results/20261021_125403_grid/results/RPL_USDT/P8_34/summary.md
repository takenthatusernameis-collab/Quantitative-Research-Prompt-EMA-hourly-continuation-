# EMA Hourly Continuation — RPL/USDT P8_34

**Symbol:** RPL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.7746 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0211 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.8328 |
| sortino_ratio | -1.1681 |
| max_drawdown | 0.7549 |
| cagr | -0.4170 |
| net_avg_win | 62.0248 |
| net_avg_loss | -77.9912 |
| avg_hold_time_bars | 9.1293 |
| exposure | 0.3450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
