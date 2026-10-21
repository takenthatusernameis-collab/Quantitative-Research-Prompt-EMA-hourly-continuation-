# EMA Hourly Continuation — CELO/USDT P144_200

**Symbol:** CELO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 201 |
| net_profit_factor | 0.5823 |
| net_win_rate | 0.4577 |
| gross_profit_factor | 0.8070 |
| gross_win_rate | 0.4577 |
| sharpe_ratio | -2.1886 |
| sortino_ratio | -0.4420 |
| max_drawdown | 0.4361 |
| cagr | -0.1836 |
| net_avg_win | 60.6818 |
| net_avg_loss | -87.9644 |
| avg_hold_time_bars | 7.1642 |
| exposure | 0.0652 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
