# EMA Hourly Continuation — DEXE/USDT P34_50

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.6151 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.8832 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -2.4129 |
| sortino_ratio | -0.5595 |
| max_drawdown | 0.4894 |
| cagr | -0.2266 |
| net_avg_win | 61.2595 |
| net_avg_loss | -88.2169 |
| avg_hold_time_bars | 13.6477 |
| exposure | 0.1638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
