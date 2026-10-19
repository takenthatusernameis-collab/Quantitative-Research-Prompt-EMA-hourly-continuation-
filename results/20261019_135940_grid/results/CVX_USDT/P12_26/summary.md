# EMA Hourly Continuation — CVX/USDT P12_26

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1443 |
| net_profit_factor | 0.3737 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7516 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -10.5656 |
| sortino_ratio | -5.6676 |
| max_drawdown | 0.9992 |
| cagr | -0.9407 |
| net_avg_win | 9.7269 |
| net_avg_loss | -19.2220 |
| avg_hold_time_bars | 2.9653 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
