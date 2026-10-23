# EMA Hourly Continuation — EDU/USDT P21_26

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1218 |
| net_profit_factor | 0.2641 |
| net_win_rate | 0.3719 |
| gross_profit_factor | 0.6780 |
| gross_win_rate | 0.4163 |
| sharpe_ratio | -12.7501 |
| sortino_ratio | -6.3842 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 7.9205 |
| net_avg_loss | -17.7583 |
| avg_hold_time_bars | 2.3350 |
| exposure | 0.1287 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
