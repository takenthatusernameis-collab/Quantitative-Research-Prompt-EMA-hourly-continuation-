# EMA Hourly Continuation — GRAM/USDT P20_55

**Symbol:** GRAM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6301 |
| net_win_rate | 0.4717 |
| gross_profit_factor | 0.9007 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -3.1190 |
| sortino_ratio | -0.9569 |
| max_drawdown | 0.6737 |
| cagr | -0.3547 |
| net_avg_win | 52.3603 |
| net_avg_loss | -74.2113 |
| avg_hold_time_bars | 8.8413 |
| exposure | 0.1849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
