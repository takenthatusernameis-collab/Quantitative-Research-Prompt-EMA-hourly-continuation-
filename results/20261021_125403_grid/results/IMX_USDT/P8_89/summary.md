# EMA Hourly Continuation — IMX/USDT P8_89

**Symbol:** IMX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.9174 |
| net_win_rate | 0.5223 |
| gross_profit_factor | 1.0874 |
| gross_win_rate | 0.5223 |
| sharpe_ratio | -0.5477 |
| sortino_ratio | -0.1748 |
| max_drawdown | 0.2505 |
| cagr | -0.0829 |
| net_avg_win | 84.4454 |
| net_avg_loss | -100.6295 |
| avg_hold_time_bars | 27.9818 |
| exposure | 0.6255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
