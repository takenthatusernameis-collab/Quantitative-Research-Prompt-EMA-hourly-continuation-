# EMA Hourly Continuation — BCH/USDT P144_200

**Symbol:** BCH/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 189 |
| net_profit_factor | 0.6983 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0425 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -1.5955 |
| sortino_ratio | -0.3161 |
| max_drawdown | 0.3271 |
| cagr | -0.1339 |
| net_avg_win | 73.0663 |
| net_avg_loss | -108.0152 |
| avg_hold_time_bars | 6.6402 |
| exposure | 0.0570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
