# EMA Hourly Continuation — DEXE/USDT P12_200

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.8169 |
| net_win_rate | 0.5271 |
| gross_profit_factor | 1.0944 |
| gross_win_rate | 0.5328 |
| sharpe_ratio | -1.0079 |
| sortino_ratio | -0.2670 |
| max_drawdown | 0.4174 |
| cagr | -0.1218 |
| net_avg_win | 67.1363 |
| net_avg_loss | -91.5895 |
| avg_hold_time_bars | 48.5812 |
| exposure | 0.7751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
