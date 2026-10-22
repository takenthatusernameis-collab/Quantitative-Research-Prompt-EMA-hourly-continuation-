# EMA Hourly Continuation — BAND/USDT P21_34

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.6858 |
| net_win_rate | 0.5065 |
| gross_profit_factor | 1.0570 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -2.9765 |
| sortino_ratio | -0.9902 |
| max_drawdown | 0.7008 |
| cagr | -0.3624 |
| net_avg_win | 54.6699 |
| net_avg_loss | -81.8259 |
| avg_hold_time_bars | 5.1140 |
| exposure | 0.1238 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
