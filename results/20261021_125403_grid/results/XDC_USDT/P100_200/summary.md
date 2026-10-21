# EMA Hourly Continuation — XDC/USDT P100_200

**Symbol:** XDC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 1.0027 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9800 |
| sortino_ratio | -0.4667 |
| max_drawdown | 0.4265 |
| cagr | -0.1931 |
| net_avg_win | 66.0486 |
| net_avg_loss | -95.7079 |
| avg_hold_time_bars | 9.7259 |
| exposure | 0.1194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
