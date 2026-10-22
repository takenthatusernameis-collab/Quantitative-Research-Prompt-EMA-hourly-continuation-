# EMA Hourly Continuation — MNT/USDT P26_50

**Symbol:** MNT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 879 |
| net_profit_factor | 0.2818 |
| net_win_rate | 0.3936 |
| gross_profit_factor | 0.6908 |
| gross_win_rate | 0.4278 |
| sharpe_ratio | -10.3170 |
| sortino_ratio | -4.3626 |
| max_drawdown | 0.9967 |
| cagr | -0.8963 |
| net_avg_win | 11.3026 |
| net_avg_loss | -26.0356 |
| avg_hold_time_bars | 4.5711 |
| exposure | 0.1826 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
