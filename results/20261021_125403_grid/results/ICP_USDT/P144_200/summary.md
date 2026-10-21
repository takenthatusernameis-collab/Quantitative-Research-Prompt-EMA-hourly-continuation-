# EMA Hourly Continuation — ICP/USDT P144_200

**Symbol:** ICP/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.5932 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8012 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -2.1928 |
| sortino_ratio | -0.4237 |
| max_drawdown | 0.3953 |
| cagr | -0.1773 |
| net_avg_win | 68.9072 |
| net_avg_loss | -93.3890 |
| avg_hold_time_bars | 6.6630 |
| exposure | 0.0557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
