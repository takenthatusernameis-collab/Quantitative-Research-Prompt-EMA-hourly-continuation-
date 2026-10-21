# EMA Hourly Continuation — FIL/USDT P34_55

**Symbol:** FIL/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.8660 |
| net_win_rate | 0.5530 |
| gross_profit_factor | 1.2233 |
| gross_win_rate | 0.5530 |
| sharpe_ratio | -0.6601 |
| sortino_ratio | -0.1557 |
| max_drawdown | 0.1753 |
| cagr | -0.0705 |
| net_avg_win | 74.1946 |
| net_avg_loss | -106.0061 |
| avg_hold_time_bars | 5.2955 |
| exposure | 0.0635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
