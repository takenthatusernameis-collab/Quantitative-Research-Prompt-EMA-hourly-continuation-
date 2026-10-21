# EMA Hourly Continuation — XRP/USDT P8_21

**Symbol:** XRP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7177 |
| net_win_rate | 0.5336 |
| gross_profit_factor | 1.1144 |
| gross_win_rate | 0.5336 |
| sharpe_ratio | -1.9541 |
| sortino_ratio | -0.5867 |
| max_drawdown | 0.5217 |
| cagr | -0.2345 |
| net_avg_win | 54.0541 |
| net_avg_loss | -86.1767 |
| avg_hold_time_bars | 5.5104 |
| exposure | 0.1080 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
