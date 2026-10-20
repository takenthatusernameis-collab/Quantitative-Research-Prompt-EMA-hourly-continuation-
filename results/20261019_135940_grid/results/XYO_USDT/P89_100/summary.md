# EMA Hourly Continuation — XYO/USDT P89_100

**Symbol:** XYO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 728 |
| net_profit_factor | 0.2129 |
| net_win_rate | 0.3228 |
| gross_profit_factor | 0.7235 |
| gross_win_rate | 0.3764 |
| sharpe_ratio | -12.2905 |
| sortino_ratio | -4.9111 |
| max_drawdown | 0.9988 |
| cagr | -0.9295 |
| net_avg_win | 11.4938 |
| net_avg_loss | -25.7375 |
| avg_hold_time_bars | 2.6923 |
| exposure | 0.0887 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
