# EMA Hourly Continuation — CGPT/USDT P8_34

**Symbol:** CGPT/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1360 |
| net_profit_factor | 0.5804 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 1.0015 |
| gross_win_rate | 0.4875 |
| sharpe_ratio | -6.9866 |
| sortino_ratio | -3.6077 |
| max_drawdown | 0.9891 |
| cagr | -0.8304 |
| net_avg_win | 21.1619 |
| net_avg_loss | -32.9896 |
| avg_hold_time_bars | 5.3647 |
| exposure | 0.3316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
