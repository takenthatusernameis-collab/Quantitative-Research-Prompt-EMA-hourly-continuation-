# EMA Hourly Continuation — SKL/USDT P12_21

**Symbol:** SKL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7034 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9977 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.3488 |
| sortino_ratio | -0.6547 |
| max_drawdown | 0.5729 |
| cagr | -0.2585 |
| net_avg_win | 67.3475 |
| net_avg_loss | -93.2332 |
| avg_hold_time_bars | 4.4244 |
| exposure | 0.0758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
