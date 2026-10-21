# EMA Hourly Continuation — REQ/USDT P8_89

**Symbol:** REQ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6083 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.8241 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -4.9427 |
| sortino_ratio | -1.7691 |
| max_drawdown | 0.8775 |
| cagr | -0.5620 |
| net_avg_win | 49.7323 |
| net_avg_loss | -61.1484 |
| avg_hold_time_bars | 18.6771 |
| exposure | 0.5416 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
