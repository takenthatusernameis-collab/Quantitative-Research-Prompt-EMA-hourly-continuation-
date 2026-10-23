# EMA Hourly Continuation — ID/USDT P50_89

**Symbol:** ID/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.5069 |
| net_win_rate | 0.4721 |
| gross_profit_factor | 0.8922 |
| gross_win_rate | 0.4801 |
| sharpe_ratio | -4.6818 |
| sortino_ratio | -1.6588 |
| max_drawdown | 0.8622 |
| cagr | -0.5429 |
| net_avg_win | 29.9142 |
| net_avg_loss | -52.7699 |
| avg_hold_time_bars | 5.6555 |
| exposure | 0.1605 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
