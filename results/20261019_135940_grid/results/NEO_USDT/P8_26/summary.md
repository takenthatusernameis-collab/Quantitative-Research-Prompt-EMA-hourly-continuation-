# EMA Hourly Continuation — NEO/USDT P8_26

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1569 |
| net_profit_factor | 0.3790 |
| net_win_rate | 0.4296 |
| gross_profit_factor | 0.8245 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -11.5025 |
| sortino_ratio | -6.4358 |
| max_drawdown | 0.9997 |
| cagr | -0.9599 |
| net_avg_win | 9.0507 |
| net_avg_loss | -17.9855 |
| avg_hold_time_bars | 3.9184 |
| exposure | 0.2795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
