# EMA Hourly Continuation — BTT/USDT P12_34

**Symbol:** BTT/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 577 |
| net_profit_factor | 0.5438 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.9384 |
| gross_win_rate | 0.4610 |
| sharpe_ratio | -5.6082 |
| sortino_ratio | -1.9440 |
| max_drawdown | 0.8997 |
| cagr | -0.5956 |
| net_avg_win | 40.3512 |
| net_avg_loss | -63.0244 |
| avg_hold_time_bars | 7.7314 |
| exposure | 0.2028 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
