# EMA Hourly Continuation — POKT/USDT P21_34

**Symbol:** POKT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1207 |
| net_profit_factor | 0.3547 |
| net_win_rate | 0.3529 |
| gross_profit_factor | 0.8123 |
| gross_win_rate | 0.3819 |
| sharpe_ratio | -12.5906 |
| sortino_ratio | -6.1963 |
| max_drawdown | 0.9996 |
| cagr | -0.9558 |
| net_avg_win | 12.9000 |
| net_avg_loss | -19.8355 |
| avg_hold_time_bars | 3.3819 |
| exposure | 0.1847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
