# EMA Hourly Continuation — DGB/USDT P20_144

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 605 |
| net_profit_factor | 0.6090 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.9091 |
| gross_win_rate | 0.4579 |
| sharpe_ratio | -4.5579 |
| sortino_ratio | -1.5740 |
| max_drawdown | 0.8588 |
| cagr | -0.5301 |
| net_avg_win | 49.4063 |
| net_avg_loss | -64.5112 |
| avg_hold_time_bars | 19.3802 |
| exposure | 0.5330 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
