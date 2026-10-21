# EMA Hourly Continuation — SUI/USDT P26_34

**Symbol:** SUI/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 157 |
| net_profit_factor | 0.6292 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -1.8729 |
| sortino_ratio | -0.3350 |
| max_drawdown | 0.3650 |
| cagr | -0.1422 |
| net_avg_win | 75.3281 |
| net_avg_loss | -101.4158 |
| avg_hold_time_bars | 3.9618 |
| exposure | 0.0283 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
