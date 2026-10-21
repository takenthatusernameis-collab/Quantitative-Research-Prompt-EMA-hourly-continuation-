# EMA Hourly Continuation — ENJ/USDT P8_21

**Symbol:** ENJ/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1654 |
| net_profit_factor | 0.3575 |
| net_win_rate | 0.4293 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -11.6573 |
| sortino_ratio | -6.6595 |
| max_drawdown | 0.9998 |
| cagr | -0.9659 |
| net_avg_win | 7.8368 |
| net_avg_loss | -16.4854 |
| avg_hold_time_bars | 3.1778 |
| exposure | 0.2378 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
