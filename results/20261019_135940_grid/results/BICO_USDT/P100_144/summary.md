# EMA Hourly Continuation — BICO/USDT P100_144

**Symbol:** BICO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 463 |
| net_profit_factor | 0.5162 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8777 |
| gross_win_rate | 0.4687 |
| sharpe_ratio | -4.2799 |
| sortino_ratio | -1.2981 |
| max_drawdown | 0.8008 |
| cagr | -0.4677 |
| net_avg_win | 40.5674 |
| net_avg_loss | -64.6693 |
| avg_hold_time_bars | 5.4449 |
| exposure | 0.1146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
