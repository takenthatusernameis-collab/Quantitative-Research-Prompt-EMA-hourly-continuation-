# EMA Hourly Continuation — CHZ/USDT P21_144

**Symbol:** CHZ/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7265 |
| net_win_rate | 0.5034 |
| gross_profit_factor | 1.0800 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -2.2240 |
| sortino_ratio | -0.6606 |
| max_drawdown | 0.5665 |
| cagr | -0.2727 |
| net_avg_win | 64.9949 |
| net_avg_loss | -90.6729 |
| avg_hold_time_bars | 27.1119 |
| exposure | 0.5509 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
