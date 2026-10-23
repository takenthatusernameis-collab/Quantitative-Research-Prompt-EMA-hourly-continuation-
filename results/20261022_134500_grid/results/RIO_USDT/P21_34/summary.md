# EMA Hourly Continuation — RIO/USDT P21_34

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.3363 |
| net_win_rate | 0.3642 |
| gross_profit_factor | 0.5948 |
| gross_win_rate | 0.3748 |
| sharpe_ratio | -11.6162 |
| sortino_ratio | -5.7745 |
| max_drawdown | 0.9993 |
| cagr | -0.9463 |
| net_avg_win | 11.3050 |
| net_avg_loss | -19.2553 |
| avg_hold_time_bars | 2.6919 |
| exposure | 0.1520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
