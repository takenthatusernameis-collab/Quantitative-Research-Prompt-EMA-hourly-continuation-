# EMA Hourly Continuation — IO/USDT P12_50

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 571 |
| net_profit_factor | 0.8193 |
| net_win_rate | 0.4956 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.4956 |
| sharpe_ratio | -1.6298 |
| sortino_ratio | -0.5749 |
| max_drawdown | 0.5108 |
| cagr | -0.2341 |
| net_avg_win | 74.7765 |
| net_avg_loss | -89.6857 |
| avg_hold_time_bars | 11.4133 |
| exposure | 0.3155 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
