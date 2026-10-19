# EMA Hourly Continuation — TIA/USDT P8_100

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 586 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9871 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.8189 |
| sortino_ratio | -0.9536 |
| max_drawdown | 0.6985 |
| cagr | -0.3704 |
| net_avg_win | 61.1421 |
| net_avg_loss | -81.1908 |
| avg_hold_time_bars | 26.1724 |
| exposure | 0.6971 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
