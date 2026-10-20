# EMA Hourly Continuation — DOGS/USDT P12_100

**Symbol:** DOGS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.6832 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9815 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -2.9185 |
| sortino_ratio | -1.1120 |
| max_drawdown | 0.6804 |
| cagr | -0.4067 |
| net_avg_win | 47.0963 |
| net_avg_loss | -68.9345 |
| avg_hold_time_bars | 16.9223 |
| exposure | 0.5548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
