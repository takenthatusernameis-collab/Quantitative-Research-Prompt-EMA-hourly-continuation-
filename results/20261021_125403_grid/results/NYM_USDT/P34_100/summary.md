# EMA Hourly Continuation — NYM/USDT P34_100

**Symbol:** NYM/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.4704 |
| net_win_rate | 0.4244 |
| gross_profit_factor | 0.7338 |
| gross_win_rate | 0.4277 |
| sharpe_ratio | -3.8578 |
| sortino_ratio | -0.9662 |
| max_drawdown | 0.6846 |
| cagr | -0.3646 |
| net_avg_win | 45.7513 |
| net_avg_loss | -71.7198 |
| avg_hold_time_bars | 18.6720 |
| exposure | 0.2640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
