# EMA Hourly Continuation — ETH/USDT P50_100

**Symbol:** ETH/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.6737 |
| net_win_rate | 0.5083 |
| gross_profit_factor | 1.0349 |
| gross_win_rate | 0.5116 |
| sharpe_ratio | -2.0802 |
| sortino_ratio | -0.5199 |
| max_drawdown | 0.4773 |
| cagr | -0.2114 |
| net_avg_win | 60.6175 |
| net_avg_loss | -93.0164 |
| avg_hold_time_bars | 9.1196 |
| exposure | 0.1248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
