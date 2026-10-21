# EMA Hourly Continuation — CFX/USDT P50_144

**Symbol:** CFX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8615 |
| net_win_rate | 0.5222 |
| gross_profit_factor | 1.0768 |
| gross_win_rate | 0.5222 |
| sharpe_ratio | -0.7676 |
| sortino_ratio | -0.1964 |
| max_drawdown | 0.2302 |
| cagr | -0.0883 |
| net_avg_win | 78.0859 |
| net_avg_loss | -99.0471 |
| avg_hold_time_bars | 20.8766 |
| exposure | 0.2999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
