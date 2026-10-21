# EMA Hourly Continuation — IOTA/USDT P12_89

**Symbol:** IOTA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 559 |
| net_profit_factor | 0.7691 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9582 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -2.0387 |
| sortino_ratio | -0.6880 |
| max_drawdown | 0.5809 |
| cagr | -0.2724 |
| net_avg_win | 67.3744 |
| net_avg_loss | -83.0197 |
| avg_hold_time_bars | 20.0537 |
| exposure | 0.5095 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
