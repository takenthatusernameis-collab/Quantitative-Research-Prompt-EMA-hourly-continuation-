# EMA Hourly Continuation — ACE/USDT P21_26

**Symbol:** ACE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6414 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.3666 |
| sortino_ratio | -0.5995 |
| max_drawdown | 0.5064 |
| cagr | -0.2393 |
| net_avg_win | 57.8787 |
| net_avg_loss | -87.4016 |
| avg_hold_time_bars | 6.4345 |
| exposure | 0.0911 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
