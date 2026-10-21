# EMA Hourly Continuation — ONE/USDT P12_144

**Symbol:** ONE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.8565 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9975 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -0.9493 |
| sortino_ratio | -0.2475 |
| max_drawdown | 0.3770 |
| cagr | -0.1098 |
| net_avg_win | 91.0973 |
| net_avg_loss | -105.7246 |
| avg_hold_time_bars | 45.8378 |
| exposure | 0.6938 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
