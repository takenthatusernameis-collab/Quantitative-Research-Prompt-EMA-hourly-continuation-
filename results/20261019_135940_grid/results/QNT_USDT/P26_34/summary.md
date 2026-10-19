# EMA Hourly Continuation — QNT/USDT P26_34

**Symbol:** QNT/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1165 |
| net_profit_factor | 0.1746 |
| net_win_rate | 0.3665 |
| gross_profit_factor | 0.7083 |
| gross_win_rate | 0.4318 |
| sharpe_ratio | -14.2945 |
| sortino_ratio | -7.1344 |
| max_drawdown | 0.9999 |
| cagr | -0.9781 |
| net_avg_win | 4.9543 |
| net_avg_loss | -16.4157 |
| avg_hold_time_bars | 1.9991 |
| exposure | 0.1059 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
