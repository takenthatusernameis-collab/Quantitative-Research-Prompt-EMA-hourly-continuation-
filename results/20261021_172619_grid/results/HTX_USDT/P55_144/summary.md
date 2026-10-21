# EMA Hourly Continuation — HTX/USDT P55_144

**Symbol:** HTX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.4306 |
| net_win_rate | 0.3729 |
| gross_profit_factor | 0.6897 |
| gross_win_rate | 0.3729 |
| sharpe_ratio | -5.8181 |
| sortino_ratio | -1.5760 |
| max_drawdown | 0.8526 |
| cagr | -0.5262 |
| net_avg_win | 48.5769 |
| net_avg_loss | -67.0846 |
| avg_hold_time_bars | 16.3418 |
| exposure | 0.2618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
