# EMA Hourly Continuation — BCH/USDT P26_200

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.8956 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.1005 |
| gross_win_rate | 0.5248 |
| sharpe_ratio | -0.5183 |
| sortino_ratio | -0.1162 |
| max_drawdown | 0.2596 |
| cagr | -0.0541 |
| net_avg_win | 88.1065 |
| net_avg_loss | -108.6445 |
| avg_hold_time_bars | 57.3223 |
| exposure | 0.6305 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
