# EMA Hourly Continuation — EUL/USDT P20_100

**Symbol:** EUL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.7924 |
| net_win_rate | 0.4954 |
| gross_profit_factor | 0.9620 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -1.3941 |
| sortino_ratio | -0.4172 |
| max_drawdown | 0.4158 |
| cagr | -0.1758 |
| net_avg_win | 67.6448 |
| net_avg_loss | -83.8208 |
| avg_hold_time_bars | 19.1050 |
| exposure | 0.3804 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
