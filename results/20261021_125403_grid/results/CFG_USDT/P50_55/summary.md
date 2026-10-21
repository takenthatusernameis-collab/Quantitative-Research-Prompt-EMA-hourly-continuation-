# EMA Hourly Continuation — CFG/USDT P50_55

**Symbol:** CFG/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 118 |
| net_profit_factor | 0.8492 |
| net_win_rate | 0.5424 |
| gross_profit_factor | 1.1630 |
| gross_win_rate | 0.5424 |
| sharpe_ratio | -0.4846 |
| sortino_ratio | -0.0762 |
| max_drawdown | 0.2139 |
| cagr | -0.0351 |
| net_avg_win | 75.4796 |
| net_avg_loss | -105.3388 |
| avg_hold_time_bars | 4.9492 |
| exposure | 0.0265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
