# EMA Hourly Continuation — FIL/USDT P20_144

**Symbol:** FIL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.5977 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8921 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -3.6924 |
| sortino_ratio | -1.1661 |
| max_drawdown | 0.7639 |
| cagr | -0.4228 |
| net_avg_win | 48.5615 |
| net_avg_loss | -68.6535 |
| avg_hold_time_bars | 22.8160 |
| exposure | 0.5185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
