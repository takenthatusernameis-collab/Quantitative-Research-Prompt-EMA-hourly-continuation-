# EMA Hourly Continuation — BAT/USDT P21_144

**Symbol:** BAT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.7735 |
| net_win_rate | 0.5012 |
| gross_profit_factor | 0.9905 |
| gross_win_rate | 0.5012 |
| sharpe_ratio | -1.5805 |
| sortino_ratio | -0.4638 |
| max_drawdown | 0.4636 |
| cagr | -0.1927 |
| net_avg_win | 67.3068 |
| net_avg_loss | -87.4312 |
| avg_hold_time_bars | 27.2280 |
| exposure | 0.5210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
