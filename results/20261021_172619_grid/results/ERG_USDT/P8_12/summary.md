# EMA Hourly Continuation — ERG/USDT P8_12

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.4253 |
| net_win_rate | 0.3730 |
| gross_profit_factor | 0.6055 |
| gross_win_rate | 0.3730 |
| sharpe_ratio | -4.1687 |
| sortino_ratio | -0.9266 |
| max_drawdown | 0.6850 |
| cagr | -0.3512 |
| net_avg_win | 53.8862 |
| net_avg_loss | -75.3538 |
| avg_hold_time_bars | 6.4303 |
| exposure | 0.0713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
