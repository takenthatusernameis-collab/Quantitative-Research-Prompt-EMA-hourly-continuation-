# EMA Hourly Continuation — DEXE/USDT P34_144

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6892 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 0.9989 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -2.0582 |
| sortino_ratio | -0.5764 |
| max_drawdown | 0.5389 |
| cagr | -0.2435 |
| net_avg_win | 55.3181 |
| net_avg_loss | -81.8819 |
| avg_hold_time_bars | 28.3800 |
| exposure | 0.5160 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
