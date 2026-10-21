# EMA Hourly Continuation — GLM/USDT P144_200

**Symbol:** GLM/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.5562 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.8354 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -2.8630 |
| sortino_ratio | -0.6489 |
| max_drawdown | 0.5578 |
| cagr | -0.2576 |
| net_avg_win | 57.3961 |
| net_avg_loss | -87.9118 |
| avg_hold_time_bars | 6.3480 |
| exposure | 0.0721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
