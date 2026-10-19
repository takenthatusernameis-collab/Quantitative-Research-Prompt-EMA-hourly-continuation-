# EMA Hourly Continuation — MNT/USDT P8_89

**Symbol:** MNT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.4473 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.7746 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -5.2486 |
| sortino_ratio | -1.8895 |
| max_drawdown | 0.9094 |
| cagr | -0.6116 |
| net_avg_win | 24.2264 |
| net_avg_loss | -44.8372 |
| avg_hold_time_bars | 22.2242 |
| exposure | 0.6758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
