# EMA Hourly Continuation — ID/USDT P12_55

**Symbol:** ID/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.5387 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.9054 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -5.4691 |
| sortino_ratio | -2.2710 |
| max_drawdown | 0.9381 |
| cagr | -0.6634 |
| net_avg_win | 27.1831 |
| net_avg_loss | -42.8878 |
| avg_hold_time_bars | 10.3211 |
| exposure | 0.4087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
