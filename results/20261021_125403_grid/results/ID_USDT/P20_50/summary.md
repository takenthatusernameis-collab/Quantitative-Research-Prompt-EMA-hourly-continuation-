# EMA Hourly Continuation — ID/USDT P20_50

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.7114 |
| net_win_rate | 0.4941 |
| gross_profit_factor | 0.9873 |
| gross_win_rate | 0.4941 |
| sharpe_ratio | -2.7051 |
| sortino_ratio | -0.9448 |
| max_drawdown | 0.6723 |
| cagr | -0.3513 |
| net_avg_win | 55.5210 |
| net_avg_loss | -76.2313 |
| avg_hold_time_bars | 7.7739 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
