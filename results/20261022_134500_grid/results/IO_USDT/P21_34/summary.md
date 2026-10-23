# EMA Hourly Continuation — IO/USDT P21_34

**Symbol:** IO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1046 |
| net_profit_factor | 0.4560 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -8.5629 |
| sortino_ratio | -4.0438 |
| max_drawdown | 0.9912 |
| cagr | -0.8649 |
| net_avg_win | 17.9404 |
| net_avg_loss | -31.2474 |
| avg_hold_time_bars | 2.5306 |
| exposure | 0.1281 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
