# EMA Hourly Continuation — MOG/USDT P8_55

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 591 |
| net_profit_factor | 0.8637 |
| net_win_rate | 0.5008 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.5008 |
| sharpe_ratio | -1.2778 |
| sortino_ratio | -0.4650 |
| max_drawdown | 0.4514 |
| cagr | -0.1963 |
| net_avg_win | 84.4848 |
| net_avg_loss | -98.1483 |
| avg_hold_time_bars | 16.2098 |
| exposure | 0.4762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
