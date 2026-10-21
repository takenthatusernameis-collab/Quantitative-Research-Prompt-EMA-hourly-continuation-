# EMA Hourly Continuation — XNO/USDT P55_89

**Symbol:** XNO/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5230 |
| net_win_rate | 0.4182 |
| gross_profit_factor | 0.7089 |
| gross_win_rate | 0.4182 |
| sharpe_ratio | -3.5640 |
| sortino_ratio | -0.9196 |
| max_drawdown | 0.6605 |
| cagr | -0.3453 |
| net_avg_win | 52.0230 |
| net_avg_loss | -71.4997 |
| avg_hold_time_bars | 6.3909 |
| exposure | 0.0959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
