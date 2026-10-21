# EMA Hourly Continuation — XEC/USDT P50_144

**Symbol:** XEC/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6246 |
| net_win_rate | 0.4595 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.4595 |
| sharpe_ratio | -2.8080 |
| sortino_ratio | -0.7805 |
| max_drawdown | 0.6186 |
| cagr | -0.3027 |
| net_avg_win | 56.4748 |
| net_avg_loss | -76.8729 |
| avg_hold_time_bars | 18.0940 |
| exposure | 0.3136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
