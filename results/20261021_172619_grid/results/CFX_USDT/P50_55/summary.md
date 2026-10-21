# EMA Hourly Continuation — CFX/USDT P50_55

**Symbol:** CFX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.5712 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -1.7950 |
| sortino_ratio | -0.2687 |
| max_drawdown | 0.2757 |
| cagr | -0.1162 |
| net_avg_win | 72.5225 |
| net_avg_loss | -101.9851 |
| avg_hold_time_bars | 4.7000 |
| exposure | 0.0235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
