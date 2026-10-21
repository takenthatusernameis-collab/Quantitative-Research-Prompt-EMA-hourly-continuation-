# EMA Hourly Continuation — THETA/USDT P12_34

**Symbol:** THETA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.7232 |
| net_win_rate | 0.4883 |
| gross_profit_factor | 0.9608 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -2.5636 |
| sortino_ratio | -0.8964 |
| max_drawdown | 0.6692 |
| cagr | -0.3365 |
| net_avg_win | 57.7439 |
| net_avg_loss | -76.1773 |
| avg_hold_time_bars | 6.5805 |
| exposure | 0.1783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
