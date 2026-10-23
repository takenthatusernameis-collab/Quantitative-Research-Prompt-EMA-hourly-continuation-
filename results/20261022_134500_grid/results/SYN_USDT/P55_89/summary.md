# EMA Hourly Continuation — SYN/USDT P55_89

**Symbol:** SYN/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5498 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9574 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -4.8376 |
| sortino_ratio | -1.7514 |
| max_drawdown | 0.8837 |
| cagr | -0.5722 |
| net_avg_win | 34.9535 |
| net_avg_loss | -55.6243 |
| avg_hold_time_bars | 4.9348 |
| exposure | 0.1480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
