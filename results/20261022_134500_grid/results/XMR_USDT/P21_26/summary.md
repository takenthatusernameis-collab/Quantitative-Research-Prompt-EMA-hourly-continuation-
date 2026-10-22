# EMA Hourly Continuation — XMR/USDT P21_26

**Symbol:** XMR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1527 |
| net_profit_factor | 0.0672 |
| net_win_rate | 0.2718 |
| gross_profit_factor | 0.3755 |
| gross_win_rate | 0.3255 |
| sharpe_ratio | -20.9137 |
| sortino_ratio | -12.4018 |
| max_drawdown | 1.0000 |
| cagr | -0.9990 |
| net_avg_win | 1.7366 |
| net_avg_loss | -9.6409 |
| avg_hold_time_bars | 1.5029 |
| exposure | 0.1043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
