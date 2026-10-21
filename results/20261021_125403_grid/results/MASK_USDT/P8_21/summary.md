# EMA Hourly Continuation — MASK/USDT P8_21

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 685 |
| net_profit_factor | 0.6511 |
| net_win_rate | 0.4964 |
| gross_profit_factor | 1.0325 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -3.7389 |
| sortino_ratio | -1.4008 |
| max_drawdown | 0.8104 |
| cagr | -0.4774 |
| net_avg_win | 44.1230 |
| net_avg_loss | -66.7887 |
| avg_hold_time_bars | 6.5577 |
| exposure | 0.2042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
