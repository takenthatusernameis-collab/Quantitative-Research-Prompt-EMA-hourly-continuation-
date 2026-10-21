# EMA Hourly Continuation — AMP/USDT P12_34

**Symbol:** AMP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.4468 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.6299 |
| gross_win_rate | 0.3770 |
| sharpe_ratio | -6.5649 |
| sortino_ratio | -2.3198 |
| max_drawdown | 0.9342 |
| cagr | -0.6602 |
| net_avg_win | 32.3637 |
| net_avg_loss | -43.8339 |
| avg_hold_time_bars | 6.5631 |
| exposure | 0.1844 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
