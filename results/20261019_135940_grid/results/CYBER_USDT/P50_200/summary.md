# EMA Hourly Continuation — CYBER/USDT P50_200

**Symbol:** CYBER/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6708 |
| net_win_rate | 0.4892 |
| gross_profit_factor | 0.9368 |
| gross_win_rate | 0.4946 |
| sharpe_ratio | -2.0852 |
| sortino_ratio | -0.5696 |
| max_drawdown | 0.5273 |
| cagr | -0.2351 |
| net_avg_win | 54.8447 |
| net_avg_loss | -78.3167 |
| avg_hold_time_bars | 23.2312 |
| exposure | 0.3928 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
