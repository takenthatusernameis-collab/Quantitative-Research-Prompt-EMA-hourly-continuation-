# EMA Hourly Continuation — XLM/USDT P21_26

**Symbol:** XLM/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1206 |
| net_profit_factor | 0.0953 |
| net_win_rate | 0.3217 |
| gross_profit_factor | 0.6773 |
| gross_win_rate | 0.4121 |
| sharpe_ratio | -16.7920 |
| sortino_ratio | -8.8083 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 2.7147 |
| net_avg_loss | -13.5125 |
| avg_hold_time_bars | 1.7902 |
| exposure | 0.0981 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
