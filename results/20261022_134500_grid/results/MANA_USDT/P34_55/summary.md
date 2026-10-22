# EMA Hourly Continuation — MANA/USDT P34_55

**Symbol:** MANA/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.4444 |
| net_win_rate | 0.4166 |
| gross_profit_factor | 0.9310 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -9.2058 |
| sortino_ratio | -3.9319 |
| max_drawdown | 0.9935 |
| cagr | -0.8631 |
| net_avg_win | 21.0719 |
| net_avg_loss | -33.8567 |
| avg_hold_time_bars | 3.2287 |
| exposure | 0.1328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
