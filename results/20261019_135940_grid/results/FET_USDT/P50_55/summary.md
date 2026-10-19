# EMA Hourly Continuation — FET/USDT P50_55

**Symbol:** FET/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.2069 |
| net_win_rate | 0.3563 |
| gross_profit_factor | 0.5422 |
| gross_win_rate | 0.3968 |
| sharpe_ratio | -12.0543 |
| sortino_ratio | -5.0020 |
| max_drawdown | 0.9989 |
| cagr | -0.9337 |
| net_avg_win | 8.9857 |
| net_avg_loss | -24.0360 |
| avg_hold_time_bars | 1.8870 |
| exposure | 0.0698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
