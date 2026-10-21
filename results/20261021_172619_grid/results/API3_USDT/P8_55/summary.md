# EMA Hourly Continuation — API3/USDT P8_55

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 711 |
| net_profit_factor | 0.8143 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.7434 |
| sortino_ratio | -0.6666 |
| max_drawdown | 0.5581 |
| cagr | -0.2656 |
| net_avg_win | 65.7222 |
| net_avg_loss | -82.7773 |
| avg_hold_time_bars | 14.5570 |
| exposure | 0.4705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
