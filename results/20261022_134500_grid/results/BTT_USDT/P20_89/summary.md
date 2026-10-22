# EMA Hourly Continuation — BTT/USDT P20_89

**Symbol:** BTT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.3550 |
| net_win_rate | 0.3584 |
| gross_profit_factor | 0.7185 |
| gross_win_rate | 0.4021 |
| sharpe_ratio | -9.7841 |
| sortino_ratio | -3.6298 |
| max_drawdown | 0.9913 |
| cagr | -0.8489 |
| net_avg_win | 22.9288 |
| net_avg_loss | -36.0801 |
| avg_hold_time_bars | 14.6898 |
| exposure | 0.4434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
