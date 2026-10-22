# EMA Hourly Continuation — SKY/USDT P34_144

**Symbol:** SKY/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.5959 |
| net_win_rate | 0.4584 |
| gross_profit_factor | 0.9078 |
| gross_win_rate | 0.4703 |
| sharpe_ratio | -3.9431 |
| sortino_ratio | -1.2566 |
| max_drawdown | 0.7636 |
| cagr | -0.4539 |
| net_avg_win | 54.2608 |
| net_avg_loss | -77.0778 |
| avg_hold_time_bars | 17.3563 |
| exposure | 0.4074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
