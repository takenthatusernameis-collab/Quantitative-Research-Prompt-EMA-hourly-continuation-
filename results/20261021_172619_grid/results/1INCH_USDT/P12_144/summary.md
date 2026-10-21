# EMA Hourly Continuation — 1INCH/USDT P12_144

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 274 |
| net_profit_factor | 0.7594 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9319 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -1.4263 |
| sortino_ratio | -0.3364 |
| max_drawdown | 0.3691 |
| cagr | -0.1446 |
| net_avg_win | 77.5617 |
| net_avg_loss | -94.9441 |
| avg_hold_time_bars | 62.1934 |
| exposure | 0.7746 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
