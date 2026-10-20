# EMA Hourly Continuation — ONT/USDT P20_144

**Symbol:** ONT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.6477 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4822 |
| sharpe_ratio | -2.7646 |
| sortino_ratio | -0.8784 |
| max_drawdown | 0.6525 |
| cagr | -0.3373 |
| net_avg_win | 49.0495 |
| net_avg_loss | -69.4221 |
| avg_hold_time_bars | 23.4051 |
| exposure | 0.5359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
