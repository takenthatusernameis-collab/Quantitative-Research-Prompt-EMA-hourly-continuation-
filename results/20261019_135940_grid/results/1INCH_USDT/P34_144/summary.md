# EMA Hourly Continuation — 1INCH/USDT P34_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.5912 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.9302 |
| gross_win_rate | 0.4786 |
| sharpe_ratio | -3.8715 |
| sortino_ratio | -1.2035 |
| max_drawdown | 0.7809 |
| cagr | -0.4417 |
| net_avg_win | 48.9647 |
| net_avg_loss | -71.2172 |
| avg_hold_time_bars | 20.5153 |
| exposure | 0.4579 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
