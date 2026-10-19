# EMA Hourly Continuation — XLM/USDT P144_200

**Symbol:** XLM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.2575 |
| net_win_rate | 0.3599 |
| gross_profit_factor | 0.6611 |
| gross_win_rate | 0.3961 |
| sharpe_ratio | -7.3527 |
| sortino_ratio | -2.1434 |
| max_drawdown | 0.9357 |
| cagr | -0.6628 |
| net_avg_win | 21.7547 |
| net_avg_loss | -47.5060 |
| avg_hold_time_bars | 3.8937 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
