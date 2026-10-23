# EMA Hourly Continuation — GMX/USDT P8_20

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.4032 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.8751 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -11.4039 |
| sortino_ratio | -6.2594 |
| max_drawdown | 0.9996 |
| cagr | -0.9560 |
| net_avg_win | 10.5835 |
| net_avg_loss | -19.2510 |
| avg_hold_time_bars | 3.7725 |
| exposure | 0.2586 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
