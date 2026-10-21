# EMA Hourly Continuation — JTO/USDT P89_100

**Symbol:** JTO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 116 |
| net_profit_factor | 0.6863 |
| net_win_rate | 0.4914 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4914 |
| sharpe_ratio | -1.2178 |
| sortino_ratio | -0.1882 |
| max_drawdown | 0.2311 |
| cagr | -0.0821 |
| net_avg_win | 74.2897 |
| net_avg_loss | -104.5774 |
| avg_hold_time_bars | 4.8190 |
| exposure | 0.0254 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
