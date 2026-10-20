# EMA Hourly Continuation — NYM/USDT P21_144

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.3708 |
| net_win_rate | 0.3734 |
| gross_profit_factor | 0.6305 |
| gross_win_rate | 0.3924 |
| sharpe_ratio | -6.4805 |
| sortino_ratio | -1.9861 |
| max_drawdown | 0.9163 |
| cagr | -0.6263 |
| net_avg_win | 30.4859 |
| net_avg_loss | -48.9962 |
| avg_hold_time_bars | 24.1392 |
| exposure | 0.5201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
