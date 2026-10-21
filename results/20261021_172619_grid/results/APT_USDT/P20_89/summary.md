# EMA Hourly Continuation — APT/USDT P20_89

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 445 |
| net_profit_factor | 0.7782 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9636 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.5192 |
| sortino_ratio | -0.4584 |
| max_drawdown | 0.4657 |
| cagr | -0.1910 |
| net_avg_win | 65.5051 |
| net_avg_loss | -83.0509 |
| avg_hold_time_bars | 18.6315 |
| exposure | 0.3769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
