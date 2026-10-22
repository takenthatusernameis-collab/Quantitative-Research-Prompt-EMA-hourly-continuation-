# EMA Hourly Continuation — SUN/USDT P26_89

**Symbol:** SUN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.3078 |
| net_win_rate | 0.3627 |
| gross_profit_factor | 0.7056 |
| gross_win_rate | 0.4101 |
| sharpe_ratio | -8.9654 |
| sortino_ratio | -3.1362 |
| max_drawdown | 0.9852 |
| cagr | -0.8111 |
| net_avg_win | 19.7278 |
| net_avg_loss | -36.4879 |
| avg_hold_time_bars | 12.0621 |
| exposure | 0.3341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
