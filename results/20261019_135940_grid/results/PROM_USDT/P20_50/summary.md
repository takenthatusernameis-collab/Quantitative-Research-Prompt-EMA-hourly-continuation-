# EMA Hourly Continuation — PROM/USDT P20_50

**Symbol:** PROM/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.4232 |
| net_win_rate | 0.3954 |
| gross_profit_factor | 0.8237 |
| gross_win_rate | 0.4331 |
| sharpe_ratio | -9.4313 |
| sortino_ratio | -4.2271 |
| max_drawdown | 0.9951 |
| cagr | -0.8795 |
| net_avg_win | 18.2953 |
| net_avg_loss | -28.2797 |
| avg_hold_time_bars | 5.3449 |
| exposure | 0.2451 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
