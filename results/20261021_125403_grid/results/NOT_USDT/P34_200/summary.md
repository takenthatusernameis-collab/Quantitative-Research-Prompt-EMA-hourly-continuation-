# EMA Hourly Continuation — NOT/USDT P34_200

**Symbol:** NOT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 267 |
| net_profit_factor | 0.7570 |
| net_win_rate | 0.4719 |
| gross_profit_factor | 0.8913 |
| gross_win_rate | 0.4719 |
| sharpe_ratio | -1.4290 |
| sortino_ratio | -0.3376 |
| max_drawdown | 0.3618 |
| cagr | -0.1444 |
| net_avg_win | 78.0170 |
| net_avg_loss | -92.0925 |
| avg_hold_time_bars | 42.9251 |
| exposure | 0.5384 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
