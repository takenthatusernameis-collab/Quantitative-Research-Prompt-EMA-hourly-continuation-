# EMA Hourly Continuation — BCH/USDT P26_89

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 429 |
| net_profit_factor | 0.6593 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.8992 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -2.7549 |
| sortino_ratio | -0.8153 |
| max_drawdown | 0.6461 |
| cagr | -0.3109 |
| net_avg_win | 57.9002 |
| net_avg_loss | -78.8881 |
| avg_hold_time_bars | 15.0490 |
| exposure | 0.2935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
