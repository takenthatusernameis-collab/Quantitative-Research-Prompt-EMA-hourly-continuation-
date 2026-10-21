# EMA Hourly Continuation — FLR/USDT P34_200

**Symbol:** FLR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.5071 |
| gross_profit_factor | 1.0172 |
| gross_win_rate | 0.5095 |
| sharpe_ratio | -1.3547 |
| sortino_ratio | -0.3979 |
| max_drawdown | 0.3749 |
| cagr | -0.1683 |
| net_avg_win | 68.6481 |
| net_avg_loss | -88.5375 |
| avg_hold_time_bars | 21.6476 |
| exposure | 0.4133 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
