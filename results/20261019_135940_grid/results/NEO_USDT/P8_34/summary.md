# EMA Hourly Continuation — NEO/USDT P8_34

**Symbol:** NEO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1385 |
| net_profit_factor | 0.4218 |
| net_win_rate | 0.4289 |
| gross_profit_factor | 0.8374 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -10.1755 |
| sortino_ratio | -5.3119 |
| max_drawdown | 0.9988 |
| cagr | -0.9302 |
| net_avg_win | 12.2652 |
| net_avg_loss | -21.8370 |
| avg_hold_time_bars | 5.5365 |
| exposure | 0.3485 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
