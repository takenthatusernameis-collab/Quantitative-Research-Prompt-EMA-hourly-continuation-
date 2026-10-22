# EMA Hourly Continuation — NOT/USDT P26_89

**Symbol:** NOT/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.8192 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 1.0053 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.3581 |
| sortino_ratio | -0.4097 |
| max_drawdown | 0.4037 |
| cagr | -0.1731 |
| net_avg_win | 77.9514 |
| net_avg_loss | -95.6005 |
| avg_hold_time_bars | 13.4755 |
| exposure | 0.2716 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
