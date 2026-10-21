# EMA Hourly Continuation — ARB/USDT P89_200

**Symbol:** ARB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.7224 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9029 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -1.5724 |
| sortino_ratio | -0.3441 |
| max_drawdown | 0.3404 |
| cagr | -0.1467 |
| net_avg_win | 76.3542 |
| net_avg_loss | -95.4646 |
| avg_hold_time_bars | 16.6568 |
| exposure | 0.1787 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
