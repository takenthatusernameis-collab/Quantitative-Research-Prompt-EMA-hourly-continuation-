# EMA Hourly Continuation — PUNDIX/USDT P34_50

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 896 |
| net_profit_factor | 0.3586 |
| net_win_rate | 0.4241 |
| gross_profit_factor | 0.8268 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -9.2575 |
| sortino_ratio | -3.9496 |
| max_drawdown | 0.9936 |
| cagr | -0.8641 |
| net_avg_win | 14.6169 |
| net_avg_loss | -30.0152 |
| avg_hold_time_bars | 3.7958 |
| exposure | 0.1546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
