# EMA Hourly Continuation — ICP/USDT P100_200

**Symbol:** ICP/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 248 |
| net_profit_factor | 0.8517 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0886 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.7444 |
| sortino_ratio | -0.1689 |
| max_drawdown | 0.2485 |
| cagr | -0.0763 |
| net_avg_win | 79.8590 |
| net_avg_loss | -103.3033 |
| avg_hold_time_bars | 13.5605 |
| exposure | 0.1529 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
