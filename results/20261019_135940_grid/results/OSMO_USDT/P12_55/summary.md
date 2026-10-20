# EMA Hourly Continuation — OSMO/USDT P12_55

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1005 |
| net_profit_factor | 0.5913 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -7.0887 |
| sortino_ratio | -3.1666 |
| max_drawdown | 0.9788 |
| cagr | -0.7836 |
| net_avg_win | 32.1789 |
| net_avg_loss | -42.3799 |
| avg_hold_time_bars | 8.4866 |
| exposure | 0.3877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
