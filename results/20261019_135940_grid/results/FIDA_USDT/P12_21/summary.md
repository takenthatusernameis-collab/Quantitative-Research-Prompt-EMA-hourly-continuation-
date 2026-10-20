# EMA Hourly Continuation — FIDA/USDT P12_21

**Symbol:** FIDA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1396 |
| net_profit_factor | 0.3249 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.7151 |
| gross_win_rate | 0.4413 |
| sharpe_ratio | -11.2110 |
| sortino_ratio | -5.9613 |
| max_drawdown | 0.9994 |
| cagr | -0.9464 |
| net_avg_win | 8.2929 |
| net_avg_loss | -18.1417 |
| avg_hold_time_bars | 3.1597 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
