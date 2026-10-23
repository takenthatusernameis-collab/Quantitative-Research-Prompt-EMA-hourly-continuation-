# EMA Hourly Continuation — G/USDT P89_100

**Symbol:** G/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.2063 |
| net_win_rate | 0.3747 |
| gross_profit_factor | 0.6694 |
| gross_win_rate | 0.4411 |
| sharpe_ratio | -8.9368 |
| sortino_ratio | -3.0202 |
| max_drawdown | 0.9656 |
| cagr | -0.7874 |
| net_avg_win | 14.3368 |
| net_avg_loss | -41.6507 |
| avg_hold_time_bars | 3.8201 |
| exposure | 0.0938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
