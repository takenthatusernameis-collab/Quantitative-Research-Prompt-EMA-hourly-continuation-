# EMA Hourly Continuation — MOG/USDT P8_34

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.7865 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -2.3376 |
| sortino_ratio | -0.8784 |
| max_drawdown | 0.6166 |
| cagr | -0.3336 |
| net_avg_win | 73.2365 |
| net_avg_loss | -85.8003 |
| avg_hold_time_bars | 9.6164 |
| exposure | 0.3040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
