# EMA Hourly Continuation — GMX/USDT P12_144

**Symbol:** GMX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 564 |
| net_profit_factor | 0.6525 |
| net_win_rate | 0.4699 |
| gross_profit_factor | 0.9190 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -3.3732 |
| sortino_ratio | -1.1260 |
| max_drawdown | 0.7528 |
| cagr | -0.4144 |
| net_avg_win | 52.3822 |
| net_avg_loss | -71.1452 |
| avg_hold_time_bars | 25.3546 |
| exposure | 0.6500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
