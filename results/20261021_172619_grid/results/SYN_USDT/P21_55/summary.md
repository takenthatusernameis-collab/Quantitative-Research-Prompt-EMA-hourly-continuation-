# EMA Hourly Continuation — SYN/USDT P21_55

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 547 |
| net_profit_factor | 0.7437 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -2.0866 |
| sortino_ratio | -0.6977 |
| max_drawdown | 0.5974 |
| cagr | -0.2752 |
| net_avg_win | 60.0154 |
| net_avg_loss | -77.5170 |
| avg_hold_time_bars | 8.5466 |
| exposure | 0.2125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
