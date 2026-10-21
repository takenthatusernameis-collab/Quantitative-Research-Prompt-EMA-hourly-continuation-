# EMA Hourly Continuation — RPL/USDT P12_144

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.9422 |
| net_win_rate | 0.5230 |
| gross_profit_factor | 1.0919 |
| gross_win_rate | 0.5230 |
| sharpe_ratio | -0.3043 |
| sortino_ratio | -0.0840 |
| max_drawdown | 0.2527 |
| cagr | -0.0432 |
| net_avg_win | 88.9431 |
| net_avg_loss | -103.5184 |
| avg_hold_time_bars | 42.5149 |
| exposure | 0.7100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
