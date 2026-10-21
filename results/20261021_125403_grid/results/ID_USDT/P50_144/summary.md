# EMA Hourly Continuation — ID/USDT P50_144

**Symbol:** ID/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7651 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9704 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.4530 |
| sortino_ratio | -0.4010 |
| max_drawdown | 0.3798 |
| cagr | -0.1688 |
| net_avg_win | 65.2811 |
| net_avg_loss | -84.8633 |
| avg_hold_time_bars | 16.7962 |
| exposure | 0.2835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
