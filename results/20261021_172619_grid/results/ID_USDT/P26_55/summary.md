# EMA Hourly Continuation — ID/USDT P26_55

**Symbol:** ID/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.7061 |
| net_win_rate | 0.4972 |
| gross_profit_factor | 1.0017 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -2.6041 |
| sortino_ratio | -0.8616 |
| max_drawdown | 0.6492 |
| cagr | -0.3255 |
| net_avg_win | 56.8587 |
| net_avg_loss | -79.6311 |
| avg_hold_time_bars | 7.4598 |
| exposure | 0.1806 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
