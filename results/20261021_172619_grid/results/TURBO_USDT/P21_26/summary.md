# EMA Hourly Continuation — TURBO/USDT P21_26

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 155 |
| net_profit_factor | 0.8145 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1219 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -0.8735 |
| sortino_ratio | -0.1720 |
| max_drawdown | 0.1866 |
| cagr | -0.0761 |
| net_avg_win | 81.7172 |
| net_avg_loss | -112.7031 |
| avg_hold_time_bars | 4.5806 |
| exposure | 0.0387 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
