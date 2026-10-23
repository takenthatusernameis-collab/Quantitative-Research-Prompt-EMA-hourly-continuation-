# EMA Hourly Continuation — GMT/USDT P20_21

**Symbol:** GMT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1236 |
| net_profit_factor | 0.0838 |
| net_win_rate | 0.2840 |
| gross_profit_factor | 0.5260 |
| gross_win_rate | 0.3641 |
| sharpe_ratio | -18.5228 |
| sortino_ratio | -9.9912 |
| max_drawdown | 1.0000 |
| cagr | -0.9964 |
| net_avg_win | 2.6043 |
| net_avg_loss | -12.3323 |
| avg_hold_time_bars | 1.5939 |
| exposure | 0.0895 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
