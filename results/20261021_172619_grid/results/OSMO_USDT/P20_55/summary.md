# EMA Hourly Continuation — OSMO/USDT P20_55

**Symbol:** OSMO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6684 |
| net_win_rate | 0.4622 |
| gross_profit_factor | 0.9216 |
| gross_win_rate | 0.4622 |
| sharpe_ratio | -3.4893 |
| sortino_ratio | -1.1734 |
| max_drawdown | 0.7575 |
| cagr | -0.4173 |
| net_avg_win | 58.2255 |
| net_avg_loss | -74.8749 |
| avg_hold_time_bars | 8.7788 |
| exposure | 0.2219 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
