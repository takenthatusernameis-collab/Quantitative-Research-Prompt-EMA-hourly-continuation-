# EMA Hourly Continuation — G/USDT P21_34

**Symbol:** G/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.4092 |
| net_win_rate | 0.4150 |
| gross_profit_factor | 0.9134 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -9.4077 |
| sortino_ratio | -4.2146 |
| max_drawdown | 0.9892 |
| cagr | -0.8755 |
| net_avg_win | 19.3546 |
| net_avg_loss | -33.5532 |
| avg_hold_time_bars | 4.4385 |
| exposure | 0.1991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
