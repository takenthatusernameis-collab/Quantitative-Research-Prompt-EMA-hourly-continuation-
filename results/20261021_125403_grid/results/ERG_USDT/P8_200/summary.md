# EMA Hourly Continuation — ERG/USDT P8_200

**Symbol:** ERG/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.8026 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9544 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -1.1182 |
| sortino_ratio | -0.2858 |
| max_drawdown | 0.3199 |
| cagr | -0.1246 |
| net_avg_win | 73.0929 |
| net_avg_loss | -88.8259 |
| avg_hold_time_bars | 50.9094 |
| exposure | 0.7405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
