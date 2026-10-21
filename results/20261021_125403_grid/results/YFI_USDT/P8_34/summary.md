# EMA Hourly Continuation — YFI/USDT P8_34

**Symbol:** YFI/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 864 |
| net_profit_factor | 0.5775 |
| net_win_rate | 0.4780 |
| gross_profit_factor | 0.8901 |
| gross_win_rate | 0.4780 |
| sharpe_ratio | -4.7503 |
| sortino_ratio | -1.9977 |
| max_drawdown | 0.9006 |
| cagr | -0.5996 |
| net_avg_win | 29.8033 |
| net_avg_loss | -47.2612 |
| avg_hold_time_bars | 7.8287 |
| exposure | 0.3061 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
