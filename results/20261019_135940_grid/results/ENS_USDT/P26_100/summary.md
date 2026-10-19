# EMA Hourly Continuation — ENS/USDT P26_100

**Symbol:** ENS/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6475 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -3.7213 |
| sortino_ratio | -1.3694 |
| max_drawdown | 0.8253 |
| cagr | -0.4792 |
| net_avg_win | 44.7105 |
| net_avg_loss | -65.8680 |
| avg_hold_time_bars | 11.9853 |
| exposure | 0.3694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
