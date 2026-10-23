# EMA Hourly Continuation — FLIP/USDT P26_50

**Symbol:** FLIP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.3524 |
| net_win_rate | 0.3722 |
| gross_profit_factor | 0.7338 |
| gross_win_rate | 0.4142 |
| sharpe_ratio | -8.7260 |
| sortino_ratio | -3.0772 |
| max_drawdown | 0.9828 |
| cagr | -0.7984 |
| net_avg_win | 23.2362 |
| net_avg_loss | -39.0852 |
| avg_hold_time_bars | 7.5663 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
