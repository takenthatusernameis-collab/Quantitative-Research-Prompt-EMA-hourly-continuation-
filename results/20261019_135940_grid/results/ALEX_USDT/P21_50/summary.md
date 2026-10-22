# EMA Hourly Continuation — ALEX/USDT P21_50

**Symbol:** ALEX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 827 |
| net_profit_factor | 0.4968 |
| net_win_rate | 0.3773 |
| gross_profit_factor | 0.8706 |
| gross_win_rate | 0.4015 |
| sharpe_ratio | -8.6427 |
| sortino_ratio | -3.4853 |
| max_drawdown | 0.9886 |
| cagr | -0.8278 |
| net_avg_win | 31.2660 |
| net_avg_loss | -38.1250 |
| avg_hold_time_bars | 7.2709 |
| exposure | 0.2733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
