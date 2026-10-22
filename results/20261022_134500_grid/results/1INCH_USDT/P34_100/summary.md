# EMA Hourly Continuation — 1INCH/USDT P34_100

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.5254 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.9286 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -5.4403 |
| sortino_ratio | -1.9821 |
| max_drawdown | 0.9161 |
| cagr | -0.6217 |
| net_avg_win | 32.3965 |
| net_avg_loss | -53.4368 |
| avg_hold_time_bars | 10.0967 |
| exposure | 0.3084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
