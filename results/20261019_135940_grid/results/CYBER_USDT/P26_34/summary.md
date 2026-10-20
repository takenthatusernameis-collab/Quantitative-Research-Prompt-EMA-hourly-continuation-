# EMA Hourly Continuation — CYBER/USDT P26_34

**Symbol:** CYBER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1042 |
| net_profit_factor | 0.3094 |
| net_win_rate | 0.3743 |
| gross_profit_factor | 0.7466 |
| gross_win_rate | 0.4203 |
| sharpe_ratio | -11.9056 |
| sortino_ratio | -5.5288 |
| max_drawdown | 0.9992 |
| cagr | -0.9410 |
| net_avg_win | 11.4765 |
| net_avg_loss | -22.1896 |
| avg_hold_time_bars | 2.9271 |
| exposure | 0.1386 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
