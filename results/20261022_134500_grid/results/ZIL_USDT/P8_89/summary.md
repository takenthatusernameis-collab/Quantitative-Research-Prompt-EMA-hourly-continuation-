# EMA Hourly Continuation — ZIL/USDT P8_89

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 735 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.9607 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -4.7809 |
| sortino_ratio | -1.8052 |
| max_drawdown | 0.8996 |
| cagr | -0.5896 |
| net_avg_win | 38.3993 |
| net_avg_loss | -56.3849 |
| avg_hold_time_bars | 19.0068 |
| exposure | 0.6350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
