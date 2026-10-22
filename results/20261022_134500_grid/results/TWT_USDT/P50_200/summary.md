# EMA Hourly Continuation — TWT/USDT P50_200

**Symbol:** TWT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 413 |
| net_profit_factor | 0.5752 |
| net_win_rate | 0.4649 |
| gross_profit_factor | 0.9330 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -3.3828 |
| sortino_ratio | -0.9718 |
| max_drawdown | 0.7060 |
| cagr | -0.3684 |
| net_avg_win | 48.2756 |
| net_avg_loss | -72.9169 |
| avg_hold_time_bars | 21.2349 |
| exposure | 0.3986 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
