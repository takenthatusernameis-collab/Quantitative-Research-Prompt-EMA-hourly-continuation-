# EMA Hourly Continuation — ALEX/USDT P21_34

**Symbol:** ALEX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1002 |
| net_profit_factor | 0.3866 |
| net_win_rate | 0.3413 |
| gross_profit_factor | 0.8688 |
| gross_win_rate | 0.3733 |
| sharpe_ratio | -12.1866 |
| sortino_ratio | -5.4489 |
| max_drawdown | 0.9994 |
| cagr | -0.9472 |
| net_avg_win | 18.4197 |
| net_avg_loss | -24.6869 |
| avg_hold_time_bars | 3.6297 |
| exposure | 0.1653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
