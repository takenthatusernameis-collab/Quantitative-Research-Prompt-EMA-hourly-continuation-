# EMA Hourly Continuation — XYO/USDT P8_20

**Symbol:** XYO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.5046 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7457 |
| gross_win_rate | 0.4115 |
| sharpe_ratio | -5.7141 |
| sortino_ratio | -1.9537 |
| max_drawdown | 0.8993 |
| cagr | -0.5963 |
| net_avg_win | 38.6092 |
| net_avg_loss | -53.4975 |
| avg_hold_time_bars | 5.8420 |
| exposure | 0.1523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
