# EMA Hourly Continuation — MNT/USDT P21_26

**Symbol:** MNT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 214 |
| net_profit_factor | 0.4795 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8089 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -3.3090 |
| sortino_ratio | -0.6955 |
| max_drawdown | 0.5641 |
| cagr | -0.2756 |
| net_avg_win | 53.2553 |
| net_avg_loss | -90.3549 |
| avg_hold_time_bars | 5.0140 |
| exposure | 0.0488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
