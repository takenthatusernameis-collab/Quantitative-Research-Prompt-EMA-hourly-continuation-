# EMA Hourly Continuation — ENS/USDT P89_100

**Symbol:** ENS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 102 |
| net_profit_factor | 0.5455 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4412 |
| sharpe_ratio | -1.9108 |
| sortino_ratio | -0.2758 |
| max_drawdown | 0.2798 |
| cagr | -0.1194 |
| net_avg_win | 72.9423 |
| net_avg_loss | -105.5586 |
| avg_hold_time_bars | 6.5196 |
| exposure | 0.0302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
