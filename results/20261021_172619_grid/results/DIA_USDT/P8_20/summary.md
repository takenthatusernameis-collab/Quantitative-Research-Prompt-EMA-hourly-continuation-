# EMA Hourly Continuation — DIA/USDT P8_20

**Symbol:** DIA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.6425 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9237 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -3.4914 |
| sortino_ratio | -1.3186 |
| max_drawdown | 0.7828 |
| cagr | -0.4531 |
| net_avg_win | 41.3244 |
| net_avg_loss | -61.4269 |
| avg_hold_time_bars | 5.2773 |
| exposure | 0.1662 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
