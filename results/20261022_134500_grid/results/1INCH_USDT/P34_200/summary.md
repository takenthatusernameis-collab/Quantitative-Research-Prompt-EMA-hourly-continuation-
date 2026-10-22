# EMA Hourly Continuation — 1INCH/USDT P34_200

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 276 |
| net_profit_factor | 0.8176 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1800 |
| gross_win_rate | 0.5435 |
| sharpe_ratio | -0.9576 |
| sortino_ratio | -0.2274 |
| max_drawdown | 0.2781 |
| cagr | -0.1012 |
| net_avg_win | 71.1800 |
| net_avg_loss | -100.6595 |
| avg_hold_time_bars | 51.5797 |
| exposure | 0.6471 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
