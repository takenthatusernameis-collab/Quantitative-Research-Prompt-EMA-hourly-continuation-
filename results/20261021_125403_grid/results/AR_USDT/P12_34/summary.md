# EMA Hourly Continuation — AR/USDT P12_34

**Symbol:** AR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 600 |
| net_profit_factor | 0.6699 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.8537 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -3.0516 |
| sortino_ratio | -1.0644 |
| max_drawdown | 0.7147 |
| cagr | -0.3864 |
| net_avg_win | 51.3897 |
| net_avg_loss | -66.6799 |
| avg_hold_time_bars | 7.2050 |
| exposure | 0.1965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
