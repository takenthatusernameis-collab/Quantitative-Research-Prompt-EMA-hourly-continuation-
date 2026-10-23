# EMA Hourly Continuation — ELON/USDT P12_20

**Symbol:** ELON/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1312 |
| net_profit_factor | 0.2738 |
| net_win_rate | 0.3971 |
| gross_profit_factor | 0.7434 |
| gross_win_rate | 0.4169 |
| sharpe_ratio | -12.9542 |
| sortino_ratio | -6.7786 |
| max_drawdown | 0.9998 |
| cagr | -0.9666 |
| net_avg_win | 7.2359 |
| net_avg_loss | -17.4057 |
| avg_hold_time_bars | 2.5869 |
| exposure | 0.1543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
