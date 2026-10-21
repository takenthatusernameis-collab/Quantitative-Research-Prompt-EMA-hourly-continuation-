# EMA Hourly Continuation — DGB/USDT P8_34

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.7257 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9610 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -3.1794 |
| sortino_ratio | -1.1877 |
| max_drawdown | 0.7588 |
| cagr | -0.4204 |
| net_avg_win | 60.7194 |
| net_avg_loss | -75.3243 |
| avg_hold_time_bars | 8.3834 |
| exposure | 0.2614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
