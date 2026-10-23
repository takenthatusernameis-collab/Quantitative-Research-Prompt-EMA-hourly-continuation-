# EMA Hourly Continuation — IO/USDT P8_21

**Symbol:** IO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1605 |
| net_profit_factor | 0.5439 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9086 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -9.6209 |
| sortino_ratio | -5.5906 |
| max_drawdown | 0.9984 |
| cagr | -0.9354 |
| net_avg_win | 16.4480 |
| net_avg_loss | -24.8498 |
| avg_hold_time_bars | 2.8735 |
| exposure | 0.2233 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
