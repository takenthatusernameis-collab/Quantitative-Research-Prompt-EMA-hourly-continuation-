# EMA Hourly Continuation — LINK/USDT P8_12

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1762 |
| net_profit_factor | 0.1696 |
| net_win_rate | 0.3644 |
| gross_profit_factor | 0.7322 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -18.3495 |
| sortino_ratio | -11.1686 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 3.1805 |
| net_avg_loss | -10.7517 |
| avg_hold_time_bars | 1.7230 |
| exposure | 0.1380 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
