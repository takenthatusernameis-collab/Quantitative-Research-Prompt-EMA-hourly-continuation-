# EMA Hourly Continuation — ENS/USDT P89_200

**Symbol:** ENS/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.4596 |
| net_win_rate | 0.4258 |
| gross_profit_factor | 0.7471 |
| gross_win_rate | 0.4453 |
| sharpe_ratio | -4.5034 |
| sortino_ratio | -1.2829 |
| max_drawdown | 0.8057 |
| cagr | -0.4643 |
| net_avg_win | 38.4693 |
| net_avg_loss | -62.0610 |
| avg_hold_time_bars | 10.2238 |
| exposure | 0.1910 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
