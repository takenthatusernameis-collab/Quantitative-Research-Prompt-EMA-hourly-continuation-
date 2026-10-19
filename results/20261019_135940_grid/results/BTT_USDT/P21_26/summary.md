# EMA Hourly Continuation — BTT/USDT P21_26

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1245 |
| net_profit_factor | 0.0879 |
| net_win_rate | 0.2169 |
| gross_profit_factor | 0.4879 |
| gross_win_rate | 0.3357 |
| sharpe_ratio | -21.6824 |
| sortino_ratio | -12.5700 |
| max_drawdown | 1.0000 |
| cagr | -0.9992 |
| net_avg_win | 3.5698 |
| net_avg_loss | -11.2450 |
| avg_hold_time_bars | 2.1116 |
| exposure | 0.1195 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
