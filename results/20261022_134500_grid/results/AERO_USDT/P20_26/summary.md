# EMA Hourly Continuation — AERO/USDT P20_26

**Symbol:** AERO/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1114 |
| net_profit_factor | 0.2002 |
| net_win_rate | 0.3689 |
| gross_profit_factor | 0.5024 |
| gross_win_rate | 0.4057 |
| sharpe_ratio | -13.1137 |
| sortino_ratio | -6.3176 |
| max_drawdown | 0.9998 |
| cagr | -0.9644 |
| net_avg_win | 6.0905 |
| net_avg_loss | -17.7822 |
| avg_hold_time_bars | 1.8447 |
| exposure | 0.0934 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
