# EMA Hourly Continuation — SHIB/USDT P12_89

**Symbol:** SHIB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.8141 |
| net_win_rate | 0.5089 |
| gross_profit_factor | 1.0473 |
| gross_win_rate | 0.5089 |
| sharpe_ratio | -1.6559 |
| sortino_ratio | -0.5618 |
| max_drawdown | 0.5303 |
| cagr | -0.2290 |
| net_avg_win | 73.6905 |
| net_avg_loss | -93.8080 |
| avg_hold_time_bars | 17.8643 |
| exposure | 0.4547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
