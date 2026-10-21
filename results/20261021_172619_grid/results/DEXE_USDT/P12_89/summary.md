# EMA Hourly Continuation — DEXE/USDT P12_89

**Symbol:** DEXE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.8957 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.0938 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.6328 |
| sortino_ratio | -0.1937 |
| max_drawdown | 0.3126 |
| cagr | -0.0898 |
| net_avg_win | 75.9150 |
| net_avg_loss | -94.2586 |
| avg_hold_time_bars | 29.7013 |
| exposure | 0.6102 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
