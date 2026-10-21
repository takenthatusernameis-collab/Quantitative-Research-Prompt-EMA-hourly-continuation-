# EMA Hourly Continuation — BOME/USDT P12_50

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 639 |
| net_profit_factor | 0.7544 |
| net_win_rate | 0.4757 |
| gross_profit_factor | 0.9173 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -2.4147 |
| sortino_ratio | -0.8692 |
| max_drawdown | 0.6866 |
| cagr | -0.3302 |
| net_avg_win | 64.0948 |
| net_avg_loss | -77.1017 |
| avg_hold_time_bars | 9.7997 |
| exposure | 0.2846 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
