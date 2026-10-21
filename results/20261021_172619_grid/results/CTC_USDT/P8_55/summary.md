# EMA Hourly Continuation — CTC/USDT P8_55

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 704 |
| net_profit_factor | 0.7499 |
| net_win_rate | 0.4986 |
| gross_profit_factor | 0.9835 |
| gross_win_rate | 0.4986 |
| sharpe_ratio | -2.3237 |
| sortino_ratio | -0.8826 |
| max_drawdown | 0.6783 |
| cagr | -0.3352 |
| net_avg_win | 54.7915 |
| net_avg_loss | -72.6478 |
| avg_hold_time_bars | 15.2088 |
| exposure | 0.4867 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
