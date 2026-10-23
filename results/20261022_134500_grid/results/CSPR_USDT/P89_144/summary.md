# EMA Hourly Continuation — CSPR/USDT P89_144

**Symbol:** CSPR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 689 |
| net_profit_factor | 0.4160 |
| net_win_rate | 0.3904 |
| gross_profit_factor | 0.7252 |
| gross_win_rate | 0.3948 |
| sharpe_ratio | -7.4598 |
| sortino_ratio | -2.7795 |
| max_drawdown | 0.9669 |
| cagr | -0.7396 |
| net_avg_win | 25.5815 |
| net_avg_loss | -39.3822 |
| avg_hold_time_bars | 4.8723 |
| exposure | 0.1526 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
