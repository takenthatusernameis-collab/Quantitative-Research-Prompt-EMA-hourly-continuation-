# EMA Hourly Continuation — JTO/USDT P55_100

**Symbol:** JTO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.7705 |
| net_win_rate | 0.4929 |
| gross_profit_factor | 0.9722 |
| gross_win_rate | 0.4929 |
| sharpe_ratio | -1.5173 |
| sortino_ratio | -0.4082 |
| max_drawdown | 0.4406 |
| cagr | -0.1708 |
| net_avg_win | 72.3882 |
| net_avg_loss | -91.3289 |
| avg_hold_time_bars | 7.9433 |
| exposure | 0.1275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
