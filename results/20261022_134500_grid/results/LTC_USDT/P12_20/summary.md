# EMA Hourly Continuation — LTC/USDT P12_20

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1467 |
| net_profit_factor | 0.1629 |
| net_win_rate | 0.3490 |
| gross_profit_factor | 0.8543 |
| gross_win_rate | 0.4219 |
| sharpe_ratio | -17.2786 |
| sortino_ratio | -9.7359 |
| max_drawdown | 1.0000 |
| cagr | -0.9950 |
| net_avg_win | 3.8009 |
| net_avg_loss | -12.5090 |
| avg_hold_time_bars | 1.9632 |
| exposure | 0.1309 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
