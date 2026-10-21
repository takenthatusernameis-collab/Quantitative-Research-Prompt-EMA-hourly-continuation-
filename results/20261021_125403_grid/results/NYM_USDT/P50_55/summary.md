# EMA Hourly Continuation — NYM/USDT P50_55

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 142 |
| net_profit_factor | 0.3034 |
| net_win_rate | 0.3662 |
| gross_profit_factor | 0.5557 |
| gross_win_rate | 0.3732 |
| sharpe_ratio | -3.8513 |
| sortino_ratio | -0.6622 |
| max_drawdown | 0.5491 |
| cagr | -0.2718 |
| net_avg_win | 45.9994 |
| net_avg_loss | -87.5870 |
| avg_hold_time_bars | 8.2254 |
| exposure | 0.0531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
