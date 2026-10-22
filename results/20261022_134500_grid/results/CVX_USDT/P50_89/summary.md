# EMA Hourly Continuation — CVX/USDT P50_89

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 629 |
| net_profit_factor | 0.5182 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8868 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -4.8269 |
| sortino_ratio | -1.7070 |
| max_drawdown | 0.8748 |
| cagr | -0.5628 |
| net_avg_win | 32.1136 |
| net_avg_loss | -54.0391 |
| avg_hold_time_bars | 5.2242 |
| exposure | 0.1494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
