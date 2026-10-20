# EMA Hourly Continuation — HNT/USDT P12_26

**Symbol:** HNT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1446 |
| net_profit_factor | 0.3372 |
| net_win_rate | 0.3866 |
| gross_profit_factor | 0.6890 |
| gross_win_rate | 0.3983 |
| sharpe_ratio | -12.3056 |
| sortino_ratio | -6.6330 |
| max_drawdown | 0.9998 |
| cagr | -0.9631 |
| net_avg_win | 9.0979 |
| net_avg_loss | -17.0047 |
| avg_hold_time_bars | 3.0816 |
| exposure | 0.2025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
