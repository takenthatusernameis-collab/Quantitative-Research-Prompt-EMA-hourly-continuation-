# EMA Hourly Continuation — MOODENG/USDT P8_89

**Symbol:** MOODENG/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 562 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4875 |
| gross_profit_factor | 1.0018 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -2.9975 |
| sortino_ratio | -1.0976 |
| max_drawdown | 0.6701 |
| cagr | -0.4108 |
| net_avg_win | 62.6817 |
| net_avg_loss | -82.6991 |
| avg_hold_time_bars | 20.9698 |
| exposure | 0.6521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
