# EMA Hourly Continuation — MTL/USDT P20_89

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 464 |
| net_profit_factor | 0.6623 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8852 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -2.9684 |
| sortino_ratio | -0.9085 |
| max_drawdown | 0.6643 |
| cagr | -0.3428 |
| net_avg_win | 59.3001 |
| net_avg_loss | -77.9831 |
| avg_hold_time_bars | 21.8621 |
| exposure | 0.4590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
