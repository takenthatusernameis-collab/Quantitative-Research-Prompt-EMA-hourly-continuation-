# EMA Hourly Continuation — RSR/USDT P26_34

**Symbol:** RSR/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.3365 |
| net_win_rate | 0.3986 |
| gross_profit_factor | 0.7759 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -11.1853 |
| sortino_ratio | -5.1485 |
| max_drawdown | 0.9988 |
| cagr | -0.9300 |
| net_avg_win | 12.2622 |
| net_avg_loss | -24.1601 |
| avg_hold_time_bars | 2.1467 |
| exposure | 0.1011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
