# EMA Hourly Continuation — GTC/USDT P12_50

**Symbol:** GTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 985 |
| net_profit_factor | 0.6086 |
| net_win_rate | 0.4538 |
| gross_profit_factor | 0.9741 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -5.9971 |
| sortino_ratio | -2.6556 |
| max_drawdown | 0.9602 |
| cagr | -0.7166 |
| net_avg_win | 33.3187 |
| net_avg_loss | -45.4872 |
| avg_hold_time_bars | 7.8294 |
| exposure | 0.3505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
