# EMA Hourly Continuation — JST/USDT P20_34

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.3982 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.9678 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -5.1311 |
| sortino_ratio | -1.5284 |
| max_drawdown | 0.8413 |
| cagr | -0.5148 |
| net_avg_win | 27.3425 |
| net_avg_loss | -62.2211 |
| avg_hold_time_bars | 5.4262 |
| exposure | 0.1048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
