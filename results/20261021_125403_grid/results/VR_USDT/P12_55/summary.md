# EMA Hourly Continuation — VR/USDT P12_55

**Symbol:** VR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 496 |
| net_profit_factor | 0.6889 |
| net_win_rate | 0.4657 |
| gross_profit_factor | 0.8692 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -2.7044 |
| sortino_ratio | -0.8545 |
| max_drawdown | 0.6359 |
| cagr | -0.3269 |
| net_avg_win | 60.3788 |
| net_avg_loss | -76.4035 |
| avg_hold_time_bars | 15.0363 |
| exposure | 0.3390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
