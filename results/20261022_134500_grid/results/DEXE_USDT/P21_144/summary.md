# EMA Hourly Continuation — DEXE/USDT P21_144

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7322 |
| net_win_rate | 0.5090 |
| gross_profit_factor | 1.0262 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.7487 |
| sortino_ratio | -0.4868 |
| max_drawdown | 0.5106 |
| cagr | -0.2083 |
| net_avg_win | 60.9627 |
| net_avg_loss | -86.2970 |
| avg_hold_time_bars | 36.7775 |
| exposure | 0.6536 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
