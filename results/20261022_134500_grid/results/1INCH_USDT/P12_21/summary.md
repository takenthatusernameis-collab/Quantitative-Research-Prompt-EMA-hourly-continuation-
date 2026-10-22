# EMA Hourly Continuation — 1INCH/USDT P12_21

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1558 |
| net_profit_factor | 0.2307 |
| net_win_rate | 0.3864 |
| gross_profit_factor | 0.6937 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -15.0166 |
| sortino_ratio | -8.5053 |
| max_drawdown | 1.0000 |
| cagr | -0.9884 |
| net_avg_win | 4.9802 |
| net_avg_loss | -13.5962 |
| avg_hold_time_bars | 2.4461 |
| exposure | 0.1732 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
