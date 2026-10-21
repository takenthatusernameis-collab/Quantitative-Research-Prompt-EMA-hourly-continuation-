# EMA Hourly Continuation — DEXE/USDT P50_89

**Symbol:** DEXE/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.6790 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.9331 |
| sortino_ratio | -0.4842 |
| max_drawdown | 0.4461 |
| cagr | -0.1992 |
| net_avg_win | 61.0917 |
| net_avg_loss | -83.2291 |
| avg_hold_time_bars | 20.7500 |
| exposure | 0.2905 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
