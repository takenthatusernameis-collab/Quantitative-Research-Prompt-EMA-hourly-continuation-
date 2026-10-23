# EMA Hourly Continuation — MOG/USDT P12_144

**Symbol:** MOG/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 441 |
| net_profit_factor | 0.7169 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.9084 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -2.5022 |
| sortino_ratio | -0.7765 |
| max_drawdown | 0.6070 |
| cagr | -0.3055 |
| net_avg_win | 69.7131 |
| net_avg_loss | -85.2378 |
| avg_hold_time_bars | 30.9433 |
| exposure | 0.6784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
