# EMA Hourly Continuation — FIL/USDT P8_34

**Symbol:** FIL/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 655 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -2.0508 |
| sortino_ratio | -0.7537 |
| max_drawdown | 0.5963 |
| cagr | -0.2927 |
| net_avg_win | 56.1810 |
| net_avg_loss | -75.3261 |
| avg_hold_time_bars | 9.9618 |
| exposure | 0.2966 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
