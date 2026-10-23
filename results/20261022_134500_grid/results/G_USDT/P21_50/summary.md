# EMA Hourly Continuation — G/USDT P21_50

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 760 |
| net_profit_factor | 0.4787 |
| net_win_rate | 0.4395 |
| gross_profit_factor | 0.8654 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -6.9083 |
| sortino_ratio | -2.9069 |
| max_drawdown | 0.9511 |
| cagr | -0.7510 |
| net_avg_win | 26.1521 |
| net_avg_loss | -42.8312 |
| avg_hold_time_bars | 6.7053 |
| exposure | 0.2680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
