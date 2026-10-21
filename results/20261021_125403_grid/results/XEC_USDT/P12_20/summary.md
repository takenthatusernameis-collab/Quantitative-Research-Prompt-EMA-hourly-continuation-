# EMA Hourly Continuation — XEC/USDT P12_20

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 523 |
| net_profit_factor | 0.4960 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8086 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -5.0064 |
| sortino_ratio | -1.6425 |
| max_drawdown | 0.8555 |
| cagr | -0.5300 |
| net_avg_win | 35.9456 |
| net_avg_loss | -58.2289 |
| avg_hold_time_bars | 4.7380 |
| exposure | 0.1121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
