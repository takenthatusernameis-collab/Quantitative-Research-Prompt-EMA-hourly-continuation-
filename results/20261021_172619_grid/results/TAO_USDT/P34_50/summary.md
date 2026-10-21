# EMA Hourly Continuation — TAO/USDT P34_50

**Symbol:** TAO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 192 |
| net_profit_factor | 0.7043 |
| net_win_rate | 0.4740 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -1.6331 |
| sortino_ratio | -0.3233 |
| max_drawdown | 0.3702 |
| cagr | -0.1376 |
| net_avg_win | 81.2743 |
| net_avg_loss | -103.9749 |
| avg_hold_time_bars | 5.9323 |
| exposure | 0.0518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
