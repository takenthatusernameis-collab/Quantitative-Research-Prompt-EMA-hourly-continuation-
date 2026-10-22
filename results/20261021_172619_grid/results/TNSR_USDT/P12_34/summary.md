# EMA Hourly Continuation — TNSR/USDT P12_34

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.8189 |
| net_win_rate | 0.5115 |
| gross_profit_factor | 1.0761 |
| gross_win_rate | 0.5115 |
| sharpe_ratio | -1.9317 |
| sortino_ratio | -0.7074 |
| max_drawdown | 0.5901 |
| cagr | -0.2783 |
| net_avg_win | 75.9080 |
| net_avg_loss | -97.0534 |
| avg_hold_time_bars | 6.3905 |
| exposure | 0.1888 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
