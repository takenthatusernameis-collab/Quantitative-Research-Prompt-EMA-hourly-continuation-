# EMA Hourly Continuation — SEI/USDT P12_100

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.7582 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 1.0548 |
| gross_win_rate | 0.5041 |
| sharpe_ratio | -2.5324 |
| sortino_ratio | -0.8882 |
| max_drawdown | 0.6916 |
| cagr | -0.3415 |
| net_avg_win | 66.3698 |
| net_avg_loss | -88.3990 |
| avg_hold_time_bars | 21.2913 |
| exposure | 0.5913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
