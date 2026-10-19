# EMA Hourly Continuation — ARB/USDT P89_200

**Symbol:** ARB/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.5846 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9409 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -3.1802 |
| sortino_ratio | -0.8623 |
| max_drawdown | 0.6527 |
| cagr | -0.3416 |
| net_avg_win | 50.2632 |
| net_avg_loss | -81.0759 |
| avg_hold_time_bars | 11.0507 |
| exposure | 0.1884 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
