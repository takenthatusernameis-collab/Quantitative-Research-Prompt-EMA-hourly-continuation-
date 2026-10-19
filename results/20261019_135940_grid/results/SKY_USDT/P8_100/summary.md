# EMA Hourly Continuation — SKY/USDT P8_100

**Symbol:** SKY/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6192 |
| net_win_rate | 0.4564 |
| gross_profit_factor | 0.9177 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -4.5422 |
| sortino_ratio | -1.6506 |
| max_drawdown | 0.8411 |
| cagr | -0.5493 |
| net_avg_win | 52.1197 |
| net_avg_loss | -70.6557 |
| avg_hold_time_bars | 21.1964 |
| exposure | 0.6501 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
