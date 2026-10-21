# EMA Hourly Continuation — IMX/USDT P20_55

**Symbol:** IMX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.7991 |
| net_win_rate | 0.5037 |
| gross_profit_factor | 1.0172 |
| gross_win_rate | 0.5037 |
| sharpe_ratio | -1.6503 |
| sortino_ratio | -0.5459 |
| max_drawdown | 0.5249 |
| cagr | -0.2227 |
| net_avg_win | 69.5396 |
| net_avg_loss | -88.3350 |
| avg_hold_time_bars | 8.8015 |
| exposure | 0.2127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
