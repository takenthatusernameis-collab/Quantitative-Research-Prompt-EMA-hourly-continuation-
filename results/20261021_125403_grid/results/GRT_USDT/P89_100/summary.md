# EMA Hourly Continuation — GRT/USDT P89_100

**Symbol:** GRT/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 100 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0748 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -0.8497 |
| sortino_ratio | -0.1224 |
| max_drawdown | 0.1391 |
| cagr | -0.0543 |
| net_avg_win | 77.2174 |
| net_avg_loss | -111.0019 |
| avg_hold_time_bars | 4.1500 |
| exposure | 0.0188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
