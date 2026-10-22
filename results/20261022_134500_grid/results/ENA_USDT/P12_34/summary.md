# EMA Hourly Continuation — ENA/USDT P12_34

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1298 |
| net_profit_factor | 0.5765 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.8939 |
| gross_win_rate | 0.4769 |
| sharpe_ratio | -6.3715 |
| sortino_ratio | -3.2291 |
| max_drawdown | 0.9807 |
| cagr | -0.7887 |
| net_avg_win | 21.6874 |
| net_avg_loss | -33.8743 |
| avg_hold_time_bars | 3.9869 |
| exposure | 0.2352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
