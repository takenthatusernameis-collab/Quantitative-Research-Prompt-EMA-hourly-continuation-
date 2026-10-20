# EMA Hourly Continuation — PUFFER/USDT P100_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.5336 |
| net_win_rate | 0.4659 |
| gross_profit_factor | 0.8744 |
| gross_win_rate | 0.4688 |
| sharpe_ratio | -3.9690 |
| sortino_ratio | -1.1751 |
| max_drawdown | 0.6816 |
| cagr | -0.4285 |
| net_avg_win | 47.1997 |
| net_avg_loss | -77.1581 |
| avg_hold_time_bars | 5.0369 |
| exposure | 0.1003 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
