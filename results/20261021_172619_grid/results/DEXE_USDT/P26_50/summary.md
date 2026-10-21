# EMA Hourly Continuation — DEXE/USDT P26_50

**Symbol:** DEXE/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6761 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9254 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.2193 |
| sortino_ratio | -0.6165 |
| max_drawdown | 0.5175 |
| cagr | -0.2459 |
| net_avg_win | 57.9177 |
| net_avg_loss | -80.8064 |
| avg_hold_time_bars | 13.8037 |
| exposure | 0.2365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
