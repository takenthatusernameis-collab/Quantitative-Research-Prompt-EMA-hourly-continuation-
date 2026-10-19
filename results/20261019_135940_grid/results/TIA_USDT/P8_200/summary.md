# EMA Hourly Continuation — TIA/USDT P8_200

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8343 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0630 |
| gross_win_rate | 0.5171 |
| sharpe_ratio | -1.0382 |
| sortino_ratio | -0.2777 |
| max_drawdown | 0.3580 |
| cagr | -0.1225 |
| net_avg_win | 78.2817 |
| net_avg_loss | -99.3474 |
| avg_hold_time_bars | 51.0343 |
| exposure | 0.8119 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
