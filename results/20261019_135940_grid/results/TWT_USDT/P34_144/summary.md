# EMA Hourly Continuation — TWT/USDT P34_144

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.5037 |
| net_win_rate | 0.4501 |
| gross_profit_factor | 0.8418 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -4.8496 |
| sortino_ratio | -1.5892 |
| max_drawdown | 0.8702 |
| cagr | -0.5445 |
| net_avg_win | 35.2421 |
| net_avg_loss | -57.2672 |
| avg_hold_time_bars | 15.3975 |
| exposure | 0.3856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
