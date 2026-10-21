# EMA Hourly Continuation — ATOM/USDT P20_89

**Symbol:** ATOM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7999 |
| net_win_rate | 0.5136 |
| gross_profit_factor | 1.0389 |
| gross_win_rate | 0.5136 |
| sharpe_ratio | -1.4192 |
| sortino_ratio | -0.4457 |
| max_drawdown | 0.4378 |
| cagr | -0.1866 |
| net_avg_win | 66.0184 |
| net_avg_loss | -87.1589 |
| avg_hold_time_bars | 17.0042 |
| exposure | 0.3687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
