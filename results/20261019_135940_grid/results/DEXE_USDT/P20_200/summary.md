# EMA Hourly Continuation — DEXE/USDT P20_200

**Symbol:** DEXE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7855 |
| net_win_rate | 0.5124 |
| gross_profit_factor | 1.0694 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -1.1260 |
| sortino_ratio | -0.2867 |
| max_drawdown | 0.4266 |
| cagr | -0.1278 |
| net_avg_win | 64.4914 |
| net_avg_loss | -86.2840 |
| avg_hold_time_bars | 48.6584 |
| exposure | 0.7122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
