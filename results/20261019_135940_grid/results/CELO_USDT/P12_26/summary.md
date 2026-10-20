# EMA Hourly Continuation — CELO/USDT P12_26

**Symbol:** CELO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1382 |
| net_profit_factor | 0.3850 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8312 |
| gross_win_rate | 0.4559 |
| sharpe_ratio | -10.4144 |
| sortino_ratio | -5.4581 |
| max_drawdown | 0.9990 |
| cagr | -0.9351 |
| net_avg_win | 10.4419 |
| net_avg_loss | -20.7466 |
| avg_hold_time_bars | 3.3741 |
| exposure | 0.2110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
