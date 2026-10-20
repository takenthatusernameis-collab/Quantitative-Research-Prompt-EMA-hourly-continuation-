# EMA Hourly Continuation — UQC/USDT P20_89

**Symbol:** UQC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.2640 |
| net_win_rate | 0.2685 |
| gross_profit_factor | 0.4806 |
| gross_win_rate | 0.3068 |
| sharpe_ratio | -8.5875 |
| sortino_ratio | -2.3330 |
| max_drawdown | 0.9640 |
| cagr | -0.7325 |
| net_avg_win | 35.2770 |
| net_avg_loss | -49.0546 |
| avg_hold_time_bars | 31.5342 |
| exposure | 0.5209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
