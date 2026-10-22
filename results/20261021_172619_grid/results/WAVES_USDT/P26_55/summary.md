# EMA Hourly Continuation — WAVES/USDT P26_55

**Symbol:** WAVES/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.5481 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -4.4301 |
| sortino_ratio | -1.3507 |
| max_drawdown | 0.7966 |
| cagr | -0.4664 |
| net_avg_win | 48.6147 |
| net_avg_loss | -68.0659 |
| avg_hold_time_bars | 6.5811 |
| exposure | 0.1364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
