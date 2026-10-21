# EMA Hourly Continuation — DEXE/USDT P12_55

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.7921 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0202 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -1.6630 |
| sortino_ratio | -0.5738 |
| max_drawdown | 0.4933 |
| cagr | -0.2333 |
| net_avg_win | 63.0860 |
| net_avg_loss | -82.1575 |
| avg_hold_time_bars | 16.4128 |
| exposure | 0.4320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
