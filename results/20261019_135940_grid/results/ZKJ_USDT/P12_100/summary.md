# EMA Hourly Continuation — ZKJ/USDT P12_100

**Symbol:** ZKJ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.2100 |
| net_win_rate | 0.3203 |
| gross_profit_factor | 0.5195 |
| gross_win_rate | 0.3643 |
| sharpe_ratio | -9.2527 |
| sortino_ratio | -2.7725 |
| max_drawdown | 0.9793 |
| cagr | -0.7825 |
| net_avg_win | 19.8533 |
| net_avg_loss | -44.5467 |
| avg_hold_time_bars | 43.6822 |
| exposure | 0.8121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
