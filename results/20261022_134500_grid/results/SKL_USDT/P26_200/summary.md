# EMA Hourly Continuation — SKL/USDT P26_200

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6863 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -2.1577 |
| sortino_ratio | -0.5583 |
| max_drawdown | 0.5540 |
| cagr | -0.2323 |
| net_avg_win | 65.9040 |
| net_avg_loss | -88.3513 |
| avg_hold_time_bars | 40.5149 |
| exposure | 0.6188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
