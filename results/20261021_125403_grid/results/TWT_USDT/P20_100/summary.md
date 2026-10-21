# EMA Hourly Continuation — TWT/USDT P20_100

**Symbol:** TWT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.8250 |
| net_win_rate | 0.5256 |
| gross_profit_factor | 1.1050 |
| gross_win_rate | 0.5256 |
| sharpe_ratio | -1.3702 |
| sortino_ratio | -0.4533 |
| max_drawdown | 0.4612 |
| cagr | -0.1891 |
| net_avg_win | 69.6761 |
| net_avg_loss | -93.5755 |
| avg_hold_time_bars | 16.1120 |
| exposure | 0.3860 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
