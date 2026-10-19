# EMA Hourly Continuation — SHIB/USDT P21_26

**Symbol:** SHIB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1126 |
| net_profit_factor | 0.1551 |
| net_win_rate | 0.3277 |
| gross_profit_factor | 0.6479 |
| gross_win_rate | 0.3988 |
| sharpe_ratio | -16.1109 |
| sortino_ratio | -8.1103 |
| max_drawdown | 1.0000 |
| cagr | -0.9891 |
| net_avg_win | 4.9735 |
| net_avg_loss | -15.6342 |
| avg_hold_time_bars | 1.7034 |
| exposure | 0.0872 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
