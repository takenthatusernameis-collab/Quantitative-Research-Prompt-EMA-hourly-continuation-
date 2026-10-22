# EMA Hourly Continuation — WAVES/USDT P55_100

**Symbol:** WAVES/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 339 |
| net_profit_factor | 0.6832 |
| net_win_rate | 0.5015 |
| gross_profit_factor | 0.9681 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.0332 |
| sortino_ratio | -0.5373 |
| max_drawdown | 0.5074 |
| cagr | -0.2182 |
| net_avg_win | 58.4887 |
| net_avg_loss | -86.1171 |
| avg_hold_time_bars | 9.4543 |
| exposure | 0.1457 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
