# EMA Hourly Continuation — NEO/USDT P20_34

**Symbol:** NEO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1163 |
| net_profit_factor | 0.2603 |
| net_win_rate | 0.3732 |
| gross_profit_factor | 0.7187 |
| gross_win_rate | 0.4119 |
| sharpe_ratio | -13.0244 |
| sortino_ratio | -6.4050 |
| max_drawdown | 0.9997 |
| cagr | -0.9624 |
| net_avg_win | 8.1041 |
| net_avg_loss | -18.5385 |
| avg_hold_time_bars | 2.8048 |
| exposure | 0.1483 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
