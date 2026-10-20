# EMA Hourly Continuation — NOT/USDT P20_55

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.5827 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -5.7476 |
| sortino_ratio | -2.5824 |
| max_drawdown | 0.9556 |
| cagr | -0.7142 |
| net_avg_win | 28.1104 |
| net_avg_loss | -44.3962 |
| avg_hold_time_bars | 4.8784 |
| exposure | 0.2262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
