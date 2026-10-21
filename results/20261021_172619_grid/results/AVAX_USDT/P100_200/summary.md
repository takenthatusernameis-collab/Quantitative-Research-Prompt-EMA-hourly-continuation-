# EMA Hourly Continuation — AVAX/USDT P100_200

**Symbol:** AVAX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.6579 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8564 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -1.9618 |
| sortino_ratio | -0.4404 |
| max_drawdown | 0.4233 |
| cagr | -0.1825 |
| net_avg_win | 65.8268 |
| net_avg_loss | -87.9260 |
| avg_hold_time_bars | 11.0645 |
| exposure | 0.1247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
