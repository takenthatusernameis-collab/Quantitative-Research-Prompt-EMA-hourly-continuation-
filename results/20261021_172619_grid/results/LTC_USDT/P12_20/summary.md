# EMA Hourly Continuation — LTC/USDT P12_20

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 211 |
| net_profit_factor | 0.6656 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 1.0409 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.0602 |
| sortino_ratio | -0.4313 |
| max_drawdown | 0.4448 |
| cagr | -0.1785 |
| net_avg_win | 73.8687 |
| net_avg_loss | -109.9361 |
| avg_hold_time_bars | 4.7441 |
| exposure | 0.0455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
