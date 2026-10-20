# EMA Hourly Continuation — ZEN/USDT P12_89

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.5739 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8690 |
| gross_win_rate | 0.4710 |
| sharpe_ratio | -4.5872 |
| sortino_ratio | -1.7267 |
| max_drawdown | 0.8783 |
| cagr | -0.5662 |
| net_avg_win | 35.9103 |
| net_avg_loss | -52.1179 |
| avg_hold_time_bars | 16.8840 |
| exposure | 0.5556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
