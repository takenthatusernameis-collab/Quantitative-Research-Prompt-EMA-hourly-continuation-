# EMA Hourly Continuation — API3/USDT P8_50

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.8001 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0142 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -2.0520 |
| sortino_ratio | -0.7958 |
| max_drawdown | 0.6130 |
| cagr | -0.3071 |
| net_avg_win | 65.4643 |
| net_avg_loss | -82.4964 |
| avg_hold_time_bars | 13.2810 |
| exposure | 0.4425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
