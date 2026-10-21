# EMA Hourly Continuation — WLD/USDT P50_144

**Symbol:** WLD/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.8569 |
| net_win_rate | 0.5064 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -0.7662 |
| sortino_ratio | -0.1947 |
| max_drawdown | 0.2344 |
| cagr | -0.0880 |
| net_avg_win | 77.7994 |
| net_avg_loss | -93.1305 |
| avg_hold_time_bars | 19.3599 |
| exposure | 0.2763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
