# EMA Hourly Continuation — ENJ/USDT P12_100

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.6753 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0239 |
| gross_win_rate | 0.5031 |
| sharpe_ratio | -3.2619 |
| sortino_ratio | -1.1648 |
| max_drawdown | 0.7689 |
| cagr | -0.4229 |
| net_avg_win | 49.1083 |
| net_avg_loss | -71.8172 |
| avg_hold_time_bars | 19.9091 |
| exposure | 0.5774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
