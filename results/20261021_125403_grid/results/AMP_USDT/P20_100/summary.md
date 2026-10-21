# EMA Hourly Continuation — AMP/USDT P20_100

**Symbol:** AMP/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.5464 |
| net_win_rate | 0.4138 |
| gross_profit_factor | 0.7088 |
| gross_win_rate | 0.4138 |
| sharpe_ratio | -4.5128 |
| sortino_ratio | -1.4982 |
| max_drawdown | 0.8347 |
| cagr | -0.5001 |
| net_avg_win | 43.5672 |
| net_avg_loss | -56.2861 |
| avg_hold_time_bars | 15.4882 |
| exposure | 0.3879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
