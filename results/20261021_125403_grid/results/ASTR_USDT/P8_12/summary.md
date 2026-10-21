# EMA Hourly Continuation — ASTR/USDT P8_12

**Symbol:** ASTR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 436 |
| net_profit_factor | 0.5898 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -3.7082 |
| sortino_ratio | -1.1107 |
| max_drawdown | 0.7289 |
| cagr | -0.4014 |
| net_avg_win | 50.1822 |
| net_avg_loss | -77.6191 |
| avg_hold_time_bars | 4.5321 |
| exposure | 0.0894 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
