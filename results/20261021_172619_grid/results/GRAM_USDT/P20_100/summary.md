# EMA Hourly Continuation — GRAM/USDT P20_100

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6583 |
| net_win_rate | 0.4696 |
| gross_profit_factor | 0.8878 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -2.7539 |
| sortino_ratio | -0.8422 |
| max_drawdown | 0.6451 |
| cagr | -0.3200 |
| net_avg_win | 55.3306 |
| net_avg_loss | -74.4072 |
| avg_hold_time_bars | 18.2717 |
| exposure | 0.3820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
