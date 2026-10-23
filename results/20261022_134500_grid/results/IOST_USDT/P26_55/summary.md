# EMA Hourly Continuation — IOST/USDT P26_55

**Symbol:** IOST/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.4481 |
| net_win_rate | 0.4448 |
| gross_profit_factor | 0.8710 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -7.4005 |
| sortino_ratio | -3.0732 |
| max_drawdown | 0.9781 |
| cagr | -0.7786 |
| net_avg_win | 20.7203 |
| net_avg_loss | -37.0483 |
| avg_hold_time_bars | 5.4472 |
| exposure | 0.2132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
