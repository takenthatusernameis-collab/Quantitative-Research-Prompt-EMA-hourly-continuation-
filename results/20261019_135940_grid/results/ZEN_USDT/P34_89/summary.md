# EMA Hourly Continuation — ZEN/USDT P34_89

**Symbol:** ZEN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.5478 |
| net_win_rate | 0.4489 |
| gross_profit_factor | 0.8902 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -5.3625 |
| sortino_ratio | -2.0567 |
| max_drawdown | 0.9205 |
| cagr | -0.6289 |
| net_avg_win | 33.2612 |
| net_avg_loss | -49.4626 |
| avg_hold_time_bars | 7.4274 |
| exposure | 0.2512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
