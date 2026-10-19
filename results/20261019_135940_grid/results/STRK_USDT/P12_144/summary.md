# EMA Hourly Continuation — STRK/USDT P12_144

**Symbol:** STRK/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.6496 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8904 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -3.2462 |
| sortino_ratio | -1.0094 |
| max_drawdown | 0.7128 |
| cagr | -0.3788 |
| net_avg_win | 57.9820 |
| net_avg_loss | -74.8293 |
| avg_hold_time_bars | 30.1881 |
| exposure | 0.6710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
