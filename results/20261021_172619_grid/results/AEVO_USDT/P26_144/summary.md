# EMA Hourly Continuation — AEVO/USDT P26_144

**Symbol:** AEVO/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.8964 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0762 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.6217 |
| sortino_ratio | -0.1714 |
| max_drawdown | 0.2174 |
| cagr | -0.0795 |
| net_avg_win | 85.0048 |
| net_avg_loss | -102.8646 |
| avg_hold_time_bars | 30.3767 |
| exposure | 0.5072 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
