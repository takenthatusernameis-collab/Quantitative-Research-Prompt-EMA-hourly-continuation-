# EMA Hourly Continuation — XAI/USDT P8_144

**Symbol:** XAI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.9328 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0841 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -0.3937 |
| sortino_ratio | -0.1038 |
| max_drawdown | 0.3286 |
| cagr | -0.0511 |
| net_avg_win | 97.7936 |
| net_avg_loss | -113.9611 |
| avg_hold_time_bars | 51.5238 |
| exposure | 0.7869 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
