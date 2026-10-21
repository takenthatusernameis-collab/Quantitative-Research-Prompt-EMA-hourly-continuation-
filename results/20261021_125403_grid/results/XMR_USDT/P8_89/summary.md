# EMA Hourly Continuation — XMR/USDT P8_89

**Symbol:** XMR/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.7598 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9853 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.9352 |
| sortino_ratio | -0.6721 |
| max_drawdown | 0.5464 |
| cagr | -0.2661 |
| net_avg_win | 58.1309 |
| net_avg_loss | -76.5033 |
| avg_hold_time_bars | 17.7517 |
| exposure | 0.4745 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
