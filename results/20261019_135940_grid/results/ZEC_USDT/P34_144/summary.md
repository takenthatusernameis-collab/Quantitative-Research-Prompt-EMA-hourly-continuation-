# EMA Hourly Continuation — ZEC/USDT P34_144

**Symbol:** ZEC/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0113 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.1787 |
| sortino_ratio | -0.6743 |
| max_drawdown | 0.5888 |
| cagr | -0.2730 |
| net_avg_win | 58.1845 |
| net_avg_loss | -81.7231 |
| avg_hold_time_bars | 15.8750 |
| exposure | 0.3464 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
