# EMA Hourly Continuation — ID/USDT P20_144

**Symbol:** ID/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9655 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -1.4401 |
| sortino_ratio | -0.4118 |
| max_drawdown | 0.3935 |
| cagr | -0.1732 |
| net_avg_win | 72.1448 |
| net_avg_loss | -88.7043 |
| avg_hold_time_bars | 31.3333 |
| exposure | 0.5700 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
