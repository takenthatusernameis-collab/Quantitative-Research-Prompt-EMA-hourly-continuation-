# EMA Hourly Continuation — JUP/USDT P26_89

**Symbol:** JUP/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.8079 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9842 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -1.4351 |
| sortino_ratio | -0.4429 |
| max_drawdown | 0.4402 |
| cagr | -0.1855 |
| net_avg_win | 72.9985 |
| net_avg_loss | -89.5852 |
| avg_hold_time_bars | 12.5536 |
| exposure | 0.2659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
