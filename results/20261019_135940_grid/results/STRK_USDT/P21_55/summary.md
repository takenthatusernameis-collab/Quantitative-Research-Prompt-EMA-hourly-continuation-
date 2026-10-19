# EMA Hourly Continuation — STRK/USDT P21_55

**Symbol:** STRK/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.5676 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9637 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -5.8013 |
| sortino_ratio | -2.5119 |
| max_drawdown | 0.9531 |
| cagr | -0.7028 |
| net_avg_win | 28.1555 |
| net_avg_loss | -43.8770 |
| avg_hold_time_bars | 4.9820 |
| exposure | 0.2142 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
