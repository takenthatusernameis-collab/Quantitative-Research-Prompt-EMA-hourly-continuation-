# EMA Hourly Continuation — SUI/USDT P20_21

**Symbol:** SUI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 109 |
| net_profit_factor | 0.8324 |
| net_win_rate | 0.5321 |
| gross_profit_factor | 1.1331 |
| gross_win_rate | 0.5321 |
| sharpe_ratio | -0.5914 |
| sortino_ratio | -0.0892 |
| max_drawdown | 0.1700 |
| cagr | -0.0404 |
| net_avg_win | 84.2903 |
| net_avg_loss | -115.1548 |
| avg_hold_time_bars | 4.4220 |
| exposure | 0.0219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
