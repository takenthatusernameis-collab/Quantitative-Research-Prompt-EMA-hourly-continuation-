# EMA Hourly Continuation — ZRX/USDT P26_200

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.7924 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9733 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.3349 |
| sortino_ratio | -0.3413 |
| max_drawdown | 0.3670 |
| cagr | -0.1469 |
| net_avg_win | 79.4825 |
| net_avg_loss | -97.2235 |
| avg_hold_time_bars | 38.2118 |
| exposure | 0.5575 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
