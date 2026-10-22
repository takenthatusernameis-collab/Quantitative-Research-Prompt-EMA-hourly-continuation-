# EMA Hourly Continuation — SUN/USDT P89_100

**Symbol:** SUN/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 598 |
| net_profit_factor | 0.1147 |
| net_win_rate | 0.2441 |
| gross_profit_factor | 0.5649 |
| gross_win_rate | 0.3763 |
| sharpe_ratio | -13.5572 |
| sortino_ratio | -5.2572 |
| max_drawdown | 0.9993 |
| cagr | -0.9445 |
| net_avg_win | 8.8638 |
| net_avg_loss | -24.9719 |
| avg_hold_time_bars | 3.0234 |
| exposure | 0.0818 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
