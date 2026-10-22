# EMA Hourly Continuation — OSMO/USDT P34_55

**Symbol:** OSMO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.5788 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8673 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -3.8163 |
| sortino_ratio | -1.0735 |
| max_drawdown | 0.7173 |
| cagr | -0.3899 |
| net_avg_win | 57.1375 |
| net_avg_loss | -78.1444 |
| avg_hold_time_bars | 6.2429 |
| exposure | 0.1098 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
