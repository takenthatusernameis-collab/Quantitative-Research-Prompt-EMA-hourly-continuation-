# EMA Hourly Continuation — ZIL/USDT P55_89

**Symbol:** ZIL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8120 |
| net_win_rate | 0.5424 |
| gross_profit_factor | 1.1673 |
| gross_win_rate | 0.5424 |
| sharpe_ratio | -1.0838 |
| sortino_ratio | -0.2854 |
| max_drawdown | 0.3075 |
| cagr | -0.1226 |
| net_avg_win | 67.5583 |
| net_avg_loss | -98.6272 |
| avg_hold_time_bars | 6.5000 |
| exposure | 0.0975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
