# EMA Hourly Continuation — ZETA/USDT P21_200

**Symbol:** ZETA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.8062 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.1069 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -1.3734 |
| sortino_ratio | -0.3583 |
| max_drawdown | 0.4708 |
| cagr | -0.1571 |
| net_avg_win | 83.2865 |
| net_avg_loss | -108.9051 |
| avg_hold_time_bars | 42.1349 |
| exposure | 0.6502 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
