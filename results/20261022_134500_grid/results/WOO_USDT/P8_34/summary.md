# EMA Hourly Continuation — WOO/USDT P8_34

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1355 |
| net_profit_factor | 0.6162 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 1.0621 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -6.8752 |
| sortino_ratio | -3.5672 |
| max_drawdown | 0.9866 |
| cagr | -0.8186 |
| net_avg_win | 25.0989 |
| net_avg_loss | -35.4971 |
| avg_hold_time_bars | 5.7225 |
| exposure | 0.3525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
