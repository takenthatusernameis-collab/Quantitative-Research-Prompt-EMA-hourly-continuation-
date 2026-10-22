# EMA Hourly Continuation — MNT/USDT P8_34

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1342 |
| net_profit_factor | 0.3238 |
| net_win_rate | 0.4165 |
| gross_profit_factor | 0.6963 |
| gross_win_rate | 0.4426 |
| sharpe_ratio | -10.9714 |
| sortino_ratio | -5.6265 |
| max_drawdown | 0.9993 |
| cagr | -0.9454 |
| net_avg_win | 8.5586 |
| net_avg_loss | -18.8729 |
| avg_hold_time_bars | 6.2437 |
| exposure | 0.3809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
