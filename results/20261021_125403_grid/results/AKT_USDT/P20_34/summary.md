# EMA Hourly Continuation — AKT/USDT P20_34

**Symbol:** AKT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6066 |
| net_win_rate | 0.4464 |
| gross_profit_factor | 0.8048 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -2.5956 |
| sortino_ratio | -0.6180 |
| max_drawdown | 0.5170 |
| cagr | -0.2468 |
| net_avg_win | 62.8131 |
| net_avg_loss | -83.5093 |
| avg_hold_time_bars | 5.8679 |
| exposure | 0.0747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
