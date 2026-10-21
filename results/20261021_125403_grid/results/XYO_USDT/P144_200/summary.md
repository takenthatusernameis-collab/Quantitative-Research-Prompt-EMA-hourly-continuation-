# EMA Hourly Continuation — XYO/USDT P144_200

**Symbol:** XYO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 252 |
| net_profit_factor | 0.5853 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8605 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -2.8400 |
| sortino_ratio | -0.6435 |
| max_drawdown | 0.5443 |
| cagr | -0.2572 |
| net_avg_win | 65.3262 |
| net_avg_loss | -92.1973 |
| avg_hold_time_bars | 6.9008 |
| exposure | 0.0787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
