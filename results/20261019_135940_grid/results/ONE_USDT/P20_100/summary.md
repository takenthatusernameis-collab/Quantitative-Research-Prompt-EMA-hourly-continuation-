# EMA Hourly Continuation — ONE/USDT P20_100

**Symbol:** ONE/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.6853 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4787 |
| sharpe_ratio | -3.7914 |
| sortino_ratio | -1.3637 |
| max_drawdown | 0.8262 |
| cagr | -0.4823 |
| net_avg_win | 56.2478 |
| net_avg_loss | -74.4669 |
| avg_hold_time_bars | 14.9529 |
| exposure | 0.4472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
