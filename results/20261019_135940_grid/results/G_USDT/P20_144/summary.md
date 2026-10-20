# EMA Hourly Continuation — G/USDT P20_144

**Symbol:** G/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.5116 |
| net_win_rate | 0.4248 |
| gross_profit_factor | 0.7753 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -4.2052 |
| sortino_ratio | -1.2381 |
| max_drawdown | 0.7466 |
| cagr | -0.4415 |
| net_avg_win | 46.6830 |
| net_avg_loss | -67.3958 |
| avg_hold_time_bars | 30.4354 |
| exposure | 0.6065 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
