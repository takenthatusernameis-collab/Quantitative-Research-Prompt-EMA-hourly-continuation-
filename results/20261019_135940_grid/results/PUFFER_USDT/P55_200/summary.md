# EMA Hourly Continuation — PUFFER/USDT P55_200

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.6480 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8785 |
| gross_win_rate | 0.4706 |
| sharpe_ratio | -2.5543 |
| sortino_ratio | -0.7016 |
| max_drawdown | 0.5117 |
| cagr | -0.2823 |
| net_avg_win | 63.2482 |
| net_avg_loss | -84.5089 |
| avg_hold_time_bars | 20.6013 |
| exposure | 0.3567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
