# EMA Hourly Continuation — JUP/USDT P21_89

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.5769 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8613 |
| gross_win_rate | 0.4601 |
| sharpe_ratio | -4.6170 |
| sortino_ratio | -1.7502 |
| max_drawdown | 0.8821 |
| cagr | -0.5661 |
| net_avg_win | 36.1375 |
| net_avg_loss | -52.4889 |
| avg_hold_time_bars | 10.4725 |
| exposure | 0.3456 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
