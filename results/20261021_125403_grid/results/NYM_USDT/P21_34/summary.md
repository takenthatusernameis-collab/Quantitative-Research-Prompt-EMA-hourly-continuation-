# EMA Hourly Continuation — NYM/USDT P21_34

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.3448 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.6963 |
| gross_win_rate | 0.4132 |
| sharpe_ratio | -5.2837 |
| sortino_ratio | -1.3881 |
| max_drawdown | 0.8113 |
| cagr | -0.4809 |
| net_avg_win | 30.7911 |
| net_avg_loss | -62.8670 |
| avg_hold_time_bars | 8.2844 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
