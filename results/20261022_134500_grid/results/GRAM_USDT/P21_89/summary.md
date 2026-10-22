# EMA Hourly Continuation — GRAM/USDT P21_89

**Symbol:** GRAM/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 784 |
| net_profit_factor | 0.4054 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.7988 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -7.0867 |
| sortino_ratio | -2.7708 |
| max_drawdown | 0.9709 |
| cagr | -0.7513 |
| net_avg_win | 19.2706 |
| net_avg_loss | -36.9756 |
| avg_hold_time_bars | 9.8304 |
| exposure | 0.3503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
