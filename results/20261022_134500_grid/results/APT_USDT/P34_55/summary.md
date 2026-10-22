# EMA Hourly Continuation — APT/USDT P34_55

**Symbol:** APT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.4522 |
| net_win_rate | 0.4547 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -8.0450 |
| sortino_ratio | -3.4481 |
| max_drawdown | 0.9877 |
| cagr | -0.8230 |
| net_avg_win | 19.5384 |
| net_avg_loss | -36.0366 |
| avg_hold_time_bars | 2.9095 |
| exposure | 0.1213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
