# EMA Hourly Continuation — ARB/USDT P21_26

**Symbol:** ARB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.5555 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7679 |
| gross_win_rate | 0.4348 |
| sharpe_ratio | -2.1177 |
| sortino_ratio | -0.3544 |
| max_drawdown | 0.3577 |
| cagr | -0.1499 |
| net_avg_win | 69.7807 |
| net_avg_loss | -96.6263 |
| avg_hold_time_bars | 5.3623 |
| exposure | 0.0336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
