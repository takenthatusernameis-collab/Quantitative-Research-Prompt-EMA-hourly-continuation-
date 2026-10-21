# EMA Hourly Continuation — AR/USDT P21_50

**Symbol:** AR/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7355 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9457 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.0797 |
| sortino_ratio | -0.6607 |
| max_drawdown | 0.5419 |
| cagr | -0.2614 |
| net_avg_win | 61.2229 |
| net_avg_loss | -80.2514 |
| avg_hold_time_bars | 7.3773 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
