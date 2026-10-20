# EMA Hourly Continuation — VR/USDT P20_34

**Symbol:** VR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1235 |
| net_profit_factor | 0.3104 |
| net_win_rate | 0.2818 |
| gross_profit_factor | 0.5913 |
| gross_win_rate | 0.3061 |
| sharpe_ratio | -17.9093 |
| sortino_ratio | -9.3308 |
| max_drawdown | 1.0000 |
| cagr | -0.9960 |
| net_avg_win | 12.9347 |
| net_avg_loss | -16.3487 |
| avg_hold_time_bars | 2.9514 |
| exposure | 0.1657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
