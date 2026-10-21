# EMA Hourly Continuation — FIL/USDT P12_100

**Symbol:** FIL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.8233 |
| net_win_rate | 0.5035 |
| gross_profit_factor | 1.0082 |
| gross_win_rate | 0.5035 |
| sharpe_ratio | -1.2398 |
| sortino_ratio | -0.3686 |
| max_drawdown | 0.4063 |
| cagr | -0.1576 |
| net_avg_win | 75.1673 |
| net_avg_loss | -92.5744 |
| avg_hold_time_bars | 29.4594 |
| exposure | 0.5771 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
