# EMA Hourly Continuation — DGB/USDT P34_144

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.6082 |
| net_win_rate | 0.4557 |
| gross_profit_factor | 0.9142 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -4.2871 |
| sortino_ratio | -1.4440 |
| max_drawdown | 0.8283 |
| cagr | -0.4996 |
| net_avg_win | 48.8344 |
| net_avg_loss | -67.2125 |
| avg_hold_time_bars | 15.2035 |
| exposure | 0.3974 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
