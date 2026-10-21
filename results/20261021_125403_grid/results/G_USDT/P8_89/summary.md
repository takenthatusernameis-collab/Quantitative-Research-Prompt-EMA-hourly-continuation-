# EMA Hourly Continuation — G/USDT P8_89

**Symbol:** G/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.7199 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4753 |
| sharpe_ratio | -2.2470 |
| sortino_ratio | -0.7266 |
| max_drawdown | 0.5667 |
| cagr | -0.2847 |
| net_avg_win | 62.6571 |
| net_avg_loss | -78.8529 |
| avg_hold_time_bars | 28.2758 |
| exposure | 0.6631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
