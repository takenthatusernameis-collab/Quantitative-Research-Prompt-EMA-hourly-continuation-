# EMA Hourly Continuation — MANA/USDT P55_200

**Symbol:** MANA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.5879 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.1721 |
| sortino_ratio | -0.8668 |
| max_drawdown | 0.6682 |
| cagr | -0.3412 |
| net_avg_win | 52.0558 |
| net_avg_loss | -79.5949 |
| avg_hold_time_bars | 25.3537 |
| exposure | 0.4333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
