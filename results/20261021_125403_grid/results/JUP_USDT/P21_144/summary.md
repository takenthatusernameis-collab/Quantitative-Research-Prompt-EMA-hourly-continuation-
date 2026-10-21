# EMA Hourly Continuation — JUP/USDT P21_144

**Symbol:** JUP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.8063 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9422 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.3128 |
| sortino_ratio | -0.3617 |
| max_drawdown | 0.3821 |
| cagr | -0.1545 |
| net_avg_win | 78.6669 |
| net_avg_loss | -92.4812 |
| avg_hold_time_bars | 28.3930 |
| exposure | 0.4827 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
