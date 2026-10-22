# EMA Hourly Continuation — MOODENG/USDT P21_26

**Symbol:** MOODENG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 167 |
| net_profit_factor | 0.4359 |
| net_win_rate | 0.3892 |
| gross_profit_factor | 0.5942 |
| gross_win_rate | 0.3892 |
| sharpe_ratio | -3.3787 |
| sortino_ratio | -0.6830 |
| max_drawdown | 0.4934 |
| cagr | -0.2713 |
| net_avg_win | 56.9852 |
| net_avg_loss | -83.3169 |
| avg_hold_time_bars | 5.6407 |
| exposure | 0.0521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
