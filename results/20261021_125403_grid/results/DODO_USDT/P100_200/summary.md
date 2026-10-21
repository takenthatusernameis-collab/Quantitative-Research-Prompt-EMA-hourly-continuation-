# EMA Hourly Continuation — DODO/USDT P100_200

**Symbol:** DODO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.5696 |
| net_win_rate | 0.4212 |
| gross_profit_factor | 0.7222 |
| gross_win_rate | 0.4242 |
| sharpe_ratio | -3.1298 |
| sortino_ratio | -0.8020 |
| max_drawdown | 0.6194 |
| cagr | -0.3093 |
| net_avg_win | 57.7721 |
| net_avg_loss | -73.8116 |
| avg_hold_time_bars | 10.7121 |
| exposure | 0.1600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
