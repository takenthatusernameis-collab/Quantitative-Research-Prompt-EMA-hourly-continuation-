# EMA Hourly Continuation — CVX/USDT P21_34

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.6727 |
| net_win_rate | 0.4901 |
| gross_profit_factor | 0.9534 |
| gross_win_rate | 0.4901 |
| sharpe_ratio | -2.2974 |
| sortino_ratio | -0.6209 |
| max_drawdown | 0.5437 |
| cagr | -0.2477 |
| net_avg_win | 60.3145 |
| net_avg_loss | -86.1970 |
| avg_hold_time_bars | 4.9380 |
| exposure | 0.0797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
