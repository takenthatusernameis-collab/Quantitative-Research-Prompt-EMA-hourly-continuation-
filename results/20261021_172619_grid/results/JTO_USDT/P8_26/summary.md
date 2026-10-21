# EMA Hourly Continuation — JTO/USDT P8_26

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 764 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0191 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -2.1833 |
| sortino_ratio | -0.8653 |
| max_drawdown | 0.6523 |
| cagr | -0.3289 |
| net_avg_win | 61.9502 |
| net_avg_loss | -78.8825 |
| avg_hold_time_bars | 6.7251 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
