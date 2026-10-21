# EMA Hourly Continuation — ENA/USDT P50_100

**Symbol:** ENA/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7863 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9478 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.3041 |
| sortino_ratio | -0.3264 |
| max_drawdown | 0.3621 |
| cagr | -0.1398 |
| net_avg_win | 77.2703 |
| net_avg_loss | -93.8851 |
| avg_hold_time_bars | 10.1824 |
| exposure | 0.1421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
