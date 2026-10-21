# EMA Hourly Continuation — MANA/USDT P26_34

**Symbol:** MANA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 187 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.5134 |
| gross_profit_factor | 1.0452 |
| gross_win_rate | 0.5134 |
| sharpe_ratio | -1.4570 |
| sortino_ratio | -0.2876 |
| max_drawdown | 0.2789 |
| cagr | -0.1221 |
| net_avg_win | 67.9403 |
| net_avg_loss | -102.3241 |
| avg_hold_time_bars | 4.5401 |
| exposure | 0.0386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
