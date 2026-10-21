# EMA Hourly Continuation — XNO/USDT P50_89

**Symbol:** XNO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.5607 |
| net_win_rate | 0.4298 |
| gross_profit_factor | 0.7533 |
| gross_win_rate | 0.4298 |
| sharpe_ratio | -3.3875 |
| sortino_ratio | -0.9082 |
| max_drawdown | 0.6583 |
| cagr | -0.3414 |
| net_avg_win | 54.1985 |
| net_avg_loss | -72.8522 |
| avg_hold_time_bars | 7.0506 |
| exposure | 0.1141 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
