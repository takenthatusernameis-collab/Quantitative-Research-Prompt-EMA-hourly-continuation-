# EMA Hourly Continuation — EUL/USDT P21_26

**Symbol:** EUL/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.1886 |
| net_win_rate | 0.3591 |
| gross_profit_factor | 0.4885 |
| gross_win_rate | 0.3879 |
| sharpe_ratio | -13.4276 |
| sortino_ratio | -6.3806 |
| max_drawdown | 0.9998 |
| cagr | -0.9654 |
| net_avg_win | 6.0206 |
| net_avg_loss | -17.8836 |
| avg_hold_time_bars | 2.5916 |
| exposure | 0.1266 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
