# EMA Hourly Continuation — XDC/USDT P55_200

**Symbol:** XDC/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7308 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0107 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -1.7408 |
| sortino_ratio | -0.4522 |
| max_drawdown | 0.4342 |
| cagr | -0.1882 |
| net_avg_win | 66.6834 |
| net_avg_loss | -92.9231 |
| avg_hold_time_bars | 18.4377 |
| exposure | 0.2757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
