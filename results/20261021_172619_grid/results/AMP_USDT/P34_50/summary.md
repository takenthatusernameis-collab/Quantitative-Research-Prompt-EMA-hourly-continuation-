# EMA Hourly Continuation — AMP/USDT P34_50

**Symbol:** AMP/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.3665 |
| net_win_rate | 0.3489 |
| gross_profit_factor | 0.5353 |
| gross_win_rate | 0.3489 |
| sharpe_ratio | -5.4520 |
| sortino_ratio | -1.3931 |
| max_drawdown | 0.8077 |
| cagr | -0.4780 |
| net_avg_win | 41.5612 |
| net_avg_loss | -60.7665 |
| avg_hold_time_bars | 5.0935 |
| exposure | 0.0743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
