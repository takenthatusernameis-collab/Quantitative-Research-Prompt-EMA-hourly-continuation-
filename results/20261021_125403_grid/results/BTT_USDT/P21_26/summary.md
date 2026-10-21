# EMA Hourly Continuation — BTT/USDT P21_26

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.3504 |
| net_win_rate | 0.3947 |
| gross_profit_factor | 0.7241 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -4.6971 |
| sortino_ratio | -0.9514 |
| max_drawdown | 0.6801 |
| cagr | -0.3637 |
| net_avg_win | 48.8077 |
| net_avg_loss | -90.8499 |
| avg_hold_time_bars | 5.4842 |
| exposure | 0.0474 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
