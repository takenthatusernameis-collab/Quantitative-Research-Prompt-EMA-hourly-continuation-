# EMA Hourly Continuation — DEGEN/USDT P8_12

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 298 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9763 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.7848 |
| sortino_ratio | -0.4406 |
| max_drawdown | 0.4908 |
| cagr | -0.1842 |
| net_avg_win | 83.2596 |
| net_avg_loss | -105.0351 |
| avg_hold_time_bars | 5.0336 |
| exposure | 0.0683 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
