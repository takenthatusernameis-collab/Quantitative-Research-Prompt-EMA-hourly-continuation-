# EMA Hourly Continuation — FIL/USDT P21_89

**Symbol:** FIL/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6608 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8389 |
| gross_win_rate | 0.4583 |
| sharpe_ratio | -2.7433 |
| sortino_ratio | -0.8322 |
| max_drawdown | 0.6311 |
| cagr | -0.3181 |
| net_avg_win | 57.5697 |
| net_avg_loss | -73.7219 |
| avg_hold_time_bars | 16.3443 |
| exposure | 0.3388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
