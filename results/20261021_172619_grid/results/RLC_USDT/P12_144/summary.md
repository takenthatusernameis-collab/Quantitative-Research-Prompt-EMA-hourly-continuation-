# EMA Hourly Continuation — RLC/USDT P12_144

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8233 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0167 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -1.1822 |
| sortino_ratio | -0.3380 |
| max_drawdown | 0.3866 |
| cagr | -0.1463 |
| net_avg_win | 75.6112 |
| net_avg_loss | -94.1663 |
| avg_hold_time_bars | 37.3584 |
| exposure | 0.6775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
