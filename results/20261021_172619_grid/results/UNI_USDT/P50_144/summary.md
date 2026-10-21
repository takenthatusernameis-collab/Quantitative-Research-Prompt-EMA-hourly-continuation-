# EMA Hourly Continuation — UNI/USDT P50_144

**Symbol:** UNI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 291 |
| net_profit_factor | 0.8826 |
| net_win_rate | 0.5258 |
| gross_profit_factor | 1.0929 |
| gross_win_rate | 0.5258 |
| sharpe_ratio | -0.5929 |
| sortino_ratio | -0.1458 |
| max_drawdown | 0.2712 |
| cagr | -0.0674 |
| net_avg_win | 78.9405 |
| net_avg_loss | -99.1642 |
| avg_hold_time_bars | 20.8007 |
| exposure | 0.2751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
