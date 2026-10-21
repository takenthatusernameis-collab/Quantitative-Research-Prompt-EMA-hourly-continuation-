# EMA Hourly Continuation — ARB/USDT P21_34

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 254 |
| net_profit_factor | 0.6833 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9493 |
| gross_win_rate | 0.4882 |
| sharpe_ratio | -1.8548 |
| sortino_ratio | -0.4240 |
| max_drawdown | 0.4130 |
| cagr | -0.1754 |
| net_avg_win | 66.7949 |
| net_avg_loss | -93.2405 |
| avg_hold_time_bars | 5.8898 |
| exposure | 0.0680 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
