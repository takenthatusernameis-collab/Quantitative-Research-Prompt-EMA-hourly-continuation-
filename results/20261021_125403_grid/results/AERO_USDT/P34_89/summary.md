# EMA Hourly Continuation — AERO/USDT P34_89

**Symbol:** AERO/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7785 |
| net_win_rate | 0.4896 |
| gross_profit_factor | 0.9507 |
| gross_win_rate | 0.4896 |
| sharpe_ratio | -1.5073 |
| sortino_ratio | -0.4221 |
| max_drawdown | 0.3918 |
| cagr | -0.1771 |
| net_avg_win | 72.3710 |
| net_avg_loss | -89.1650 |
| avg_hold_time_bars | 11.4375 |
| exposure | 0.1996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
