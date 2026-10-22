# EMA Hourly Continuation — MNT/USDT P34_50

**Symbol:** MNT/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 871 |
| net_profit_factor | 0.1763 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 0.5557 |
| gross_win_rate | 0.4179 |
| sharpe_ratio | -11.7924 |
| sortino_ratio | -5.0479 |
| max_drawdown | 0.9988 |
| cagr | -0.9321 |
| net_avg_win | 6.5760 |
| net_avg_loss | -22.2080 |
| avg_hold_time_bars | 2.9782 |
| exposure | 0.1179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
