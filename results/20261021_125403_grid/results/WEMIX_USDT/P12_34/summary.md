# EMA Hourly Continuation — WEMIX/USDT P12_34

**Symbol:** WEMIX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 406 |
| net_profit_factor | 0.5126 |
| net_win_rate | 0.3916 |
| gross_profit_factor | 0.6774 |
| gross_win_rate | 0.3916 |
| sharpe_ratio | -4.5944 |
| sortino_ratio | -1.3050 |
| max_drawdown | 0.7911 |
| cagr | -0.4581 |
| net_avg_win | 51.9476 |
| net_avg_loss | -65.2357 |
| avg_hold_time_bars | 9.8350 |
| exposure | 0.1815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
