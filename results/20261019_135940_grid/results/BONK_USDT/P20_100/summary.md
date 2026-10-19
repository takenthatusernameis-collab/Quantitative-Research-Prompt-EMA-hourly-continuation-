# EMA Hourly Continuation — BONK/USDT P20_100

**Symbol:** BONK/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.6696 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9512 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -3.4031 |
| sortino_ratio | -1.2119 |
| max_drawdown | 0.8038 |
| cagr | -0.4442 |
| net_avg_win | 50.2566 |
| net_avg_loss | -68.6528 |
| avg_hold_time_bars | 14.7112 |
| exposure | 0.4353 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
