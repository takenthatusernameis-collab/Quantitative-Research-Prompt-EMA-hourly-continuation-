# EMA Hourly Continuation — XAI/USDT P50_100

**Symbol:** XAI/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6352 |
| net_win_rate | 0.4735 |
| gross_profit_factor | 0.9575 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -4.2378 |
| sortino_ratio | -1.5476 |
| max_drawdown | 0.8528 |
| cagr | -0.5158 |
| net_avg_win | 46.6338 |
| net_avg_loss | -66.0302 |
| avg_hold_time_bars | 7.0847 |
| exposure | 0.2129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
