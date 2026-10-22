# EMA Hourly Continuation — TRADE/USDT P8_34

**Symbol:** TRADE/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1159 |
| net_profit_factor | 0.5811 |
| net_win_rate | 0.4435 |
| gross_profit_factor | 0.9481 |
| gross_win_rate | 0.4478 |
| sharpe_ratio | -7.5105 |
| sortino_ratio | -3.5746 |
| max_drawdown | 0.9896 |
| cagr | -0.8300 |
| net_avg_win | 26.6767 |
| net_avg_loss | -36.5814 |
| avg_hold_time_bars | 6.8119 |
| exposure | 0.3589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
