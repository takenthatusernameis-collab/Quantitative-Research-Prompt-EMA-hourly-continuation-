# EMA Hourly Continuation — DGB/USDT P20_26

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 173 |
| net_profit_factor | 0.6336 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8714 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -1.9040 |
| sortino_ratio | -0.3576 |
| max_drawdown | 0.3725 |
| cagr | -0.1518 |
| net_avg_win | 73.2136 |
| net_avg_loss | -99.4015 |
| avg_hold_time_bars | 7.2312 |
| exposure | 0.0569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
