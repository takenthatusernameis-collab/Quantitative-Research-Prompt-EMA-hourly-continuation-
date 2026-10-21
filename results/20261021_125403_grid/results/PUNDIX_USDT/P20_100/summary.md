# EMA Hourly Continuation — PUNDIX/USDT P20_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.7180 |
| net_win_rate | 0.4848 |
| gross_profit_factor | 0.9451 |
| gross_win_rate | 0.4848 |
| sharpe_ratio | -2.4667 |
| sortino_ratio | -0.8079 |
| max_drawdown | 0.6191 |
| cagr | -0.3101 |
| net_avg_win | 60.5484 |
| net_avg_loss | -79.3462 |
| avg_hold_time_bars | 18.4924 |
| exposure | 0.4421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
