# EMA Hourly Continuation — DEXE/USDT P34_50

**Symbol:** DEXE/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 885 |
| net_profit_factor | 0.3065 |
| net_win_rate | 0.3898 |
| gross_profit_factor | 0.7251 |
| gross_win_rate | 0.4260 |
| sharpe_ratio | -9.9826 |
| sortino_ratio | -4.2262 |
| max_drawdown | 0.9956 |
| cagr | -0.8839 |
| net_avg_win | 12.7507 |
| net_avg_loss | -26.5819 |
| avg_hold_time_bars | 5.1751 |
| exposure | 0.2082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
