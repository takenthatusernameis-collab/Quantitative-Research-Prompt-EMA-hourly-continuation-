# EMA Hourly Continuation — ID/USDT P89_200

**Symbol:** ID/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.5729 |
| net_win_rate | 0.4655 |
| gross_profit_factor | 0.8955 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -3.0978 |
| sortino_ratio | -0.8111 |
| max_drawdown | 0.6280 |
| cagr | -0.3243 |
| net_avg_win | 51.9877 |
| net_avg_loss | -79.0418 |
| avg_hold_time_bars | 13.6092 |
| exposure | 0.2143 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
