# EMA Hourly Continuation — ID/USDT P50_89

**Symbol:** ID/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.6941 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9837 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -2.3804 |
| sortino_ratio | -0.7019 |
| max_drawdown | 0.5631 |
| cagr | -0.2746 |
| net_avg_win | 59.9725 |
| net_avg_loss | -84.3913 |
| avg_hold_time_bars | 7.3976 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
