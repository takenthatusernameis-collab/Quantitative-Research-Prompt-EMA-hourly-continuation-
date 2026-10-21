# EMA Hourly Continuation — SOL/USDT P50_55

**Symbol:** SOL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 98 |
| net_profit_factor | 0.6037 |
| net_win_rate | 0.4796 |
| gross_profit_factor | 0.9138 |
| gross_win_rate | 0.4796 |
| sharpe_ratio | -1.5356 |
| sortino_ratio | -0.2178 |
| max_drawdown | 0.2309 |
| cagr | -0.0959 |
| net_avg_win | 72.5046 |
| net_avg_loss | -110.6872 |
| avg_hold_time_bars | 5.1735 |
| exposure | 0.0230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
