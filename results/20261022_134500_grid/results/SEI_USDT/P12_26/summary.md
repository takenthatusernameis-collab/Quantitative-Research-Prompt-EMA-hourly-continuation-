# EMA Hourly Continuation — SEI/USDT P12_26

**Symbol:** SEI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1384 |
| net_profit_factor | 0.4814 |
| net_win_rate | 0.4292 |
| gross_profit_factor | 0.8588 |
| gross_win_rate | 0.4501 |
| sharpe_ratio | -10.2678 |
| sortino_ratio | -5.4219 |
| max_drawdown | 0.9988 |
| cagr | -0.9307 |
| net_avg_win | 15.6098 |
| net_avg_loss | -24.3797 |
| avg_hold_time_bars | 2.9292 |
| exposure | 0.1843 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
