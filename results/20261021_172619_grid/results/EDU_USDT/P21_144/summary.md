# EMA Hourly Continuation — EDU/USDT P21_144

**Symbol:** EDU/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.8637 |
| net_win_rate | 0.5107 |
| gross_profit_factor | 1.0314 |
| gross_win_rate | 0.5107 |
| sharpe_ratio | -0.8800 |
| sortino_ratio | -0.2583 |
| max_drawdown | 0.3443 |
| cagr | -0.1155 |
| net_avg_win | 78.4885 |
| net_avg_loss | -94.8438 |
| avg_hold_time_bars | 28.6532 |
| exposure | 0.5459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
