# EMA Hourly Continuation — KMNO/USDT P21_26

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.2695 |
| net_win_rate | 0.3787 |
| gross_profit_factor | 0.7952 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -12.1378 |
| sortino_ratio | -5.5510 |
| max_drawdown | 0.9993 |
| cagr | -0.9459 |
| net_avg_win | 9.8838 |
| net_avg_loss | -22.3518 |
| avg_hold_time_bars | 2.1462 |
| exposure | 0.0976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
