# EMA Hourly Continuation — WLD/USDT P21_34

**Symbol:** WLD/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 247 |
| net_profit_factor | 0.8692 |
| net_win_rate | 0.5304 |
| gross_profit_factor | 1.1261 |
| gross_win_rate | 0.5304 |
| sharpe_ratio | -0.6765 |
| sortino_ratio | -0.1536 |
| max_drawdown | 0.2572 |
| cagr | -0.0697 |
| net_avg_win | 84.1820 |
| net_avg_loss | -109.3739 |
| avg_hold_time_bars | 4.4291 |
| exposure | 0.0497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
