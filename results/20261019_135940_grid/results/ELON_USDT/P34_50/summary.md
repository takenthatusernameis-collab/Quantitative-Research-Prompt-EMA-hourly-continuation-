# EMA Hourly Continuation — ELON/USDT P34_50

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 807 |
| net_profit_factor | 0.2520 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.6076 |
| gross_win_rate | 0.4102 |
| sharpe_ratio | -9.8121 |
| sortino_ratio | -4.0278 |
| max_drawdown | 0.9932 |
| cagr | -0.8629 |
| net_avg_win | 10.5200 |
| net_avg_loss | -27.1519 |
| avg_hold_time_bars | 2.6803 |
| exposure | 0.0983 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
