# EMA Hourly Continuation — OSMO/USDT P50_89

**Symbol:** OSMO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.5618 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.7905 |
| gross_win_rate | 0.4410 |
| sharpe_ratio | -3.5117 |
| sortino_ratio | -0.9880 |
| max_drawdown | 0.6867 |
| cagr | -0.3655 |
| net_avg_win | 50.7518 |
| net_avg_loss | -71.2785 |
| avg_hold_time_bars | 7.9487 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
