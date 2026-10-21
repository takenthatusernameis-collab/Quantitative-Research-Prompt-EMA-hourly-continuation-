# EMA Hourly Continuation — WOO/USDT P34_144

**Symbol:** WOO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.7839 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -1.5573 |
| sortino_ratio | -0.4193 |
| max_drawdown | 0.4377 |
| cagr | -0.1762 |
| net_avg_win | 80.8100 |
| net_avg_loss | -96.9235 |
| avg_hold_time_bars | 25.9132 |
| exposure | 0.4205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
