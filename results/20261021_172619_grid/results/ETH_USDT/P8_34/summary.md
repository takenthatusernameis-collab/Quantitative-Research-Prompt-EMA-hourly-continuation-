# EMA Hourly Continuation — ETH/USDT P8_34

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6529 |
| net_win_rate | 0.4992 |
| gross_profit_factor | 0.9906 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -3.2928 |
| sortino_ratio | -1.1876 |
| max_drawdown | 0.7480 |
| cagr | -0.4184 |
| net_avg_win | 44.3967 |
| net_avg_loss | -67.7882 |
| avg_hold_time_bars | 8.7702 |
| exposure | 0.2515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
