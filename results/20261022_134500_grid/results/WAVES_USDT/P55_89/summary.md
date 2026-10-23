# EMA Hourly Continuation — WAVES/USDT P55_89

**Symbol:** WAVES/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 747 |
| net_profit_factor | 0.3661 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -7.8828 |
| sortino_ratio | -3.0498 |
| max_drawdown | 0.9808 |
| cagr | -0.7867 |
| net_avg_win | 17.5628 |
| net_avg_loss | -36.3502 |
| avg_hold_time_bars | 4.5194 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
