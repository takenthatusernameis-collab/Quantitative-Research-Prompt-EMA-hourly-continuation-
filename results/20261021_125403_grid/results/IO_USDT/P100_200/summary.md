# EMA Hourly Continuation — IO/USDT P100_200

**Symbol:** IO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.8447 |
| net_win_rate | 0.5040 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5040 |
| sharpe_ratio | -0.8268 |
| sortino_ratio | -0.1933 |
| max_drawdown | 0.2341 |
| cagr | -0.0869 |
| net_avg_win | 83.3237 |
| net_avg_loss | -100.2295 |
| avg_hold_time_bars | 14.6960 |
| exposure | 0.1779 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
