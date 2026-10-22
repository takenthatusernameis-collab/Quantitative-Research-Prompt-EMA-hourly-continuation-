# EMA Hourly Continuation — ILV/USDT P55_89

**Symbol:** ILV/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 328 |
| net_profit_factor | 0.7200 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9866 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -2.0355 |
| sortino_ratio | -0.5285 |
| max_drawdown | 0.4699 |
| cagr | -0.2155 |
| net_avg_win | 72.8808 |
| net_avg_loss | -97.5870 |
| avg_hold_time_bars | 6.6433 |
| exposure | 0.0990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
