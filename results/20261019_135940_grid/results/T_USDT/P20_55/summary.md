# EMA Hourly Continuation — T/USDT P20_55

**Symbol:** T/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 774 |
| net_profit_factor | 0.5555 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.9901 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -5.8331 |
| sortino_ratio | -2.2805 |
| max_drawdown | 0.9416 |
| cagr | -0.6712 |
| net_avg_win | 32.4336 |
| net_avg_loss | -51.3023 |
| avg_hold_time_bars | 7.5142 |
| exposure | 0.2632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
