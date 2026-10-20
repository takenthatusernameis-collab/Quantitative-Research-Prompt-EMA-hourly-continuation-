# EMA Hourly Continuation — ZEN/USDT P20_34

**Symbol:** ZEN/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1234 |
| net_profit_factor | 0.3452 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8046 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -9.9909 |
| sortino_ratio | -4.9648 |
| max_drawdown | 0.9981 |
| cagr | -0.9173 |
| net_avg_win | 9.8732 |
| net_avg_loss | -21.7451 |
| avg_hold_time_bars | 2.5170 |
| exposure | 0.1412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
