# EMA Hourly Continuation — ZEN/USDT P12_200

**Symbol:** ZEN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.7833 |
| net_win_rate | 0.5212 |
| gross_profit_factor | 1.1112 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -1.0727 |
| sortino_ratio | -0.2400 |
| max_drawdown | 0.3155 |
| cagr | -0.1124 |
| net_avg_win | 69.2631 |
| net_avg_loss | -96.2713 |
| avg_hold_time_bars | 69.9498 |
| exposure | 0.8235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
