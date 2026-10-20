# EMA Hourly Continuation — ENJ/USDT P50_89

**Symbol:** ENJ/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.5491 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 1.0050 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -5.1289 |
| sortino_ratio | -1.8594 |
| max_drawdown | 0.8996 |
| cagr | -0.5956 |
| net_avg_win | 34.7896 |
| net_avg_loss | -57.8331 |
| avg_hold_time_bars | 4.9225 |
| exposure | 0.1472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
