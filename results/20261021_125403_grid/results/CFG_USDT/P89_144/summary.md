# EMA Hourly Continuation — CFG/USDT P89_144

**Symbol:** CFG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.6747 |
| net_win_rate | 0.4626 |
| gross_profit_factor | 0.8525 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -2.0044 |
| sortino_ratio | -0.4780 |
| max_drawdown | 0.4314 |
| cagr | -0.1968 |
| net_avg_win | 67.5255 |
| net_avg_loss | -86.1694 |
| avg_hold_time_bars | 7.2313 |
| exposure | 0.0924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
