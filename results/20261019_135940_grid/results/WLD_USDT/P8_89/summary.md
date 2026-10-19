# EMA Hourly Continuation — WLD/USDT P8_89

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.8043 |
| net_win_rate | 0.5199 |
| gross_profit_factor | 1.1059 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -1.8611 |
| sortino_ratio | -0.6993 |
| max_drawdown | 0.6333 |
| cagr | -0.2857 |
| net_avg_win | 64.2355 |
| net_avg_loss | -86.4988 |
| avg_hold_time_bars | 20.1111 |
| exposure | 0.6417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
