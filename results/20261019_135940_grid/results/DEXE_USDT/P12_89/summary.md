# EMA Hourly Continuation — DEXE/USDT P12_89

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6330 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9540 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -3.3590 |
| sortino_ratio | -1.1743 |
| max_drawdown | 0.7675 |
| cagr | -0.4374 |
| net_avg_win | 43.3482 |
| net_avg_loss | -64.2572 |
| avg_hold_time_bars | 21.9793 |
| exposure | 0.6274 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
