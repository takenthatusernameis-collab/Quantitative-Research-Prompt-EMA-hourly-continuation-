# EMA Hourly Continuation — EDU/USDT P12_144

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7715 |
| net_win_rate | 0.4816 |
| gross_profit_factor | 0.9152 |
| gross_win_rate | 0.4816 |
| sharpe_ratio | -1.6464 |
| sortino_ratio | -0.5023 |
| max_drawdown | 0.4510 |
| cagr | -0.2082 |
| net_avg_win | 67.6968 |
| net_avg_loss | -81.5016 |
| avg_hold_time_bars | 30.8221 |
| exposure | 0.6430 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
