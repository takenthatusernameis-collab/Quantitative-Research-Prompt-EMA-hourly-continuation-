# EMA Hourly Continuation — AXL/USDT P21_50

**Symbol:** AXL/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.6278 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.8175 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -3.9999 |
| sortino_ratio | -1.3607 |
| max_drawdown | 0.8074 |
| cagr | -0.4666 |
| net_avg_win | 53.0061 |
| net_avg_loss | -65.7285 |
| avg_hold_time_bars | 6.5415 |
| exposure | 0.1711 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
