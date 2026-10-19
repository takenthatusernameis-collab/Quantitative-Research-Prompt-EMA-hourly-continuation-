# EMA Hourly Continuation — XDC/USDT P55_89

**Symbol:** XDC/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 730 |
| net_profit_factor | 0.1990 |
| net_win_rate | 0.4027 |
| gross_profit_factor | 0.6129 |
| gross_win_rate | 0.4438 |
| sharpe_ratio | -9.7580 |
| sortino_ratio | -3.7611 |
| max_drawdown | 0.9942 |
| cagr | -0.8692 |
| net_avg_win | 8.3983 |
| net_avg_loss | -28.4601 |
| avg_hold_time_bars | 3.7411 |
| exposure | 0.1241 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
